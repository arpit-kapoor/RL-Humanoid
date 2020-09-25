import sys
import numpy as np
import math
import random
import time

import gym
#import gym_maze
from gym_unity.envs import UnityEnv


# Initialize the "maze" environment
import os
#path = os.path.join(".", "Builds", "MazeMujoco")
path = os.path.join("MazeMujoco")
# env = gym.make("maze-sample-5x5-v0")
env = UnityEnv(path)

def state_to_bucket(state):
    bucket_indice = []
    for i in range(len(state)):
        if state[i] <= STATE_BOUNDS[i][0]:
            bucket_index = 0
        elif state[i] >= STATE_BOUNDS[i][1]:
            bucket_index = NUM_BUCKETS[i] - 1
        else:
            # Mapping the state bounds to the bucket array
            bound_width = STATE_BOUNDS[i][1] - STATE_BOUNDS[i][0]
            offset = (NUM_BUCKETS[i]-1)*STATE_BOUNDS[i][0]/bound_width
            scaling = (NUM_BUCKETS[i]-1)/bound_width
            bucket_index = int(round(scaling*state[i] - offset))
        bucket_indice.append(bucket_index)
    return tuple(bucket_indice)

def select_action(state, explore_rate):
    # Select a random action
    if random.random() < explore_rate:
        action = env.action_space.sample()
    # Select the action with the highest q
    else:
        action = int(np.argmax(q_table[state]))
    return action


'''
Defining the environment related constants
'''
# Number of discrete states (bucket) per state dimension
MAZE_SIZE = (5, 5)
NUM_BUCKETS = MAZE_SIZE  # one bucket per grid

# Number of discrete actions
NUM_ACTIONS = env.action_space.n  # ["N", "S", "E", "W"]
STATE_BOUNDS = [(0.0, 4.0), (0.0, 4.0)]
MAX_T = np.prod(MAZE_SIZE, dtype=int) * 100

q_table = np.load('q_table.npy')

env.render()
 # Reset the environment
obv = env.reset()

# the initial state
state_0 = state_to_bucket(obv)
total_reward = 0

for t in range(MAX_T):

    # Select an action
    action = select_action(state_0, 0)

    # execute the action
    obv, reward, done, _ = env.step(action)

    # Observe the result
    state = state_to_bucket(obv)
    total_reward += reward
    print(state, t, total_reward)

    # # Update the Q based on the result
    # best_q = np.amax(q_table[state])
    # q_table[state_0 + (action,)] += learning_rate * (reward + discount_factor * (best_q) - q_table[state_0 + (action,)])

    env.render()
    time.sleep(1)
    # Setting up for the next iteration
    state_0 = state
    if done:
        break
env.close()
