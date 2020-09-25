import sys
import numpy as np
import math
import random

import gym
#import gym_maze
from gym_unity.envs import UnityEnv

import matplotlib.pyplot as plt


def simulate():
    # Instantiating the learning related parameters
    learning_rate = 0.8
    explore_rate = 0.8
    discount_factor = 0.99

    num_streaks = 0

    env.render()

    ep_mean_reward = []

    for episode in range(num_episodes):

        obv = env.reset()

        state_0 = get_bucket(obv)
        total_reward = 0

        for t in range(max_t):

            action = select_action(state_0, explore_rate)
            obv, reward, done, _ = env.step(action)

            state = get_bucket(obv)
            print(obv, state)
            total_reward += reward

            best_q = np.amax(q_table[state])
            
            # Bellman Eq.
            q_table[state_0 + (action,)] += learning_rate * (reward + discount_factor * (best_q) - q_table[state_0 + (action,)])

            state_0 = state

            if debug:
                print("\nEpisode = %d" % episode)
                print("t = %d" % t)
                print("Action: %d" % action)
                print("State: %s" % str(state))
                print("Reward: %f" % reward)
                print("Streaks: %d" % num_streaks)
                print("")

            if render_maze:
                env.render()

            # if env.is_game_over():
            #     sys.exit()

            if done:
                print("Episode %d finished after %f time steps with total reward = %f (streak %d)."
                      % (episode, t, total_reward, num_streaks))

                if t <= solved_t:
                    num_streaks += 1
                else:
                    num_streaks = 0
                ep_mean_reward.append(total_reward)
                break


            elif t >= max_t - 1:
                print("Episode %d timed out at %d with total reward = %f."
                      % (episode, t, total_reward))
            

        if num_streaks > streak_to_end:
            break

        # Update parameters
        explore_rate = get_explore_rate(episode)
        learning_rate = get_learning_rate(episode)

    np.save('q_table.npy', q_table)
    return ep_mean_reward

def select_action(state, explore_rate):
    if random.random() < explore_rate:
        action = env.action_space.sample()
    else:
        action = int(np.argmax(q_table[state]))
    return action


def get_explore_rate(t):
    return max(min_explore_rate, min(0.8, 1.0 - math.log10((t+1)/decay_factor)))


def get_learning_rate(t):
    return max(min_learning_rate, min(0.8, 1.0 - math.log10((t+1)/decay_factor)))


def get_bucket(state):
    bucket_indice = []
    for i in range(len(state)):
        if state[i] <= state_bounds[i][0]:
            bucket_index = 0
        elif state[i] >= state_bounds[i][1]:
            bucket_index = num_buckets[i] - 1
        else:
            bound_width = state_bounds[i][1] - state_bounds[i][0]
            offset = (num_buckets[i]-1)*state_bounds[i][0]/bound_width
            scaling = (num_buckets[i]-1)/bound_width
            bucket_index = int(round(scaling*state[i] - offset))
        bucket_indice.append(bucket_index)
    return tuple(bucket_indice)


if __name__ == "__main__":

    import os
    path =  os.path.join("MazeMujoco")
    env = UnityEnv(path)

    maze_size = (5, 5)
    num_buckets = maze_size

    num_actions = env.action_space.n  # ["N", "S", "E", "W"]
    state_bounds = [(0.0, 4.0), (0.0, 4.0)]

    min_explore_rate = 0.001
    min_learning_rate = 0.2
    decay_factor = np.prod(maze_size, dtype=float) / 10.0

    num_episodes = 50000
    max_t = np.prod(maze_size, dtype=int) * 100
    streak_to_end = 100
    solved_t = np.prod(maze_size, dtype=int)
    render_maze = False
    enable_recording = True
    debug = False

    q_table = np.zeros(num_buckets + (num_actions,), dtype=float)

    recording_folder = "/tmp/maze_q_learning"

    # if ENABLE_RECORDING:
    #     env.monitor.start(recording_folder, force=True)

    ep_total_reward = simulate()
    print(ep_total_reward)

    fig = plt.figure()
    plt.plot(np.array(ep_total_reward))
    plt.xlabel('episodes')
    plt.ylabel('Episode Mean Reward')
    plt.savefig('reward.png')
    # if ENABLE_RECORDING:
    #     env.monitor.close()
