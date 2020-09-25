import os.path, gym
import numpy as np
import tensorflow as tf
import roboschool
import mjremote
import sys
import time
from squaternion import euler2quat, quat2euler, Quaternion
from zoopolicy import ZooPolicyTensorflow



config = tf.ConfigProto(
    inter_op_parallelism_threads=1,
    intra_op_parallelism_threads=1,
    device_count = { "GPU": 0 } )
sess = tf.InteractiveSession(config=config)

env = gym.make("RoboschoolHumanoidFlagrun-v1")

policy = ZooPolicyTensorflow("mymodel1", env.observation_space, env.action_space)

frame = 0
score = 0
restart_delay = 0
if_render = False
if_comm = True
frequency = 7
freq_count = 0

if if_comm:
    conn = mjremote.mjremote()
    conn.connect()

while True:

    if if_comm:
        conn.setinit()
    obs = env.reset()
    env_obj = env.unwrapped

    while True:
        action = policy.act(obs, env)
        obs, r, done, _ = env.step(action)

        if freq_count == frequency:
            x,y = conn.gettarget()
            env_obj.set_flag(x,y)
            freq_count = 0

        pos = env_obj.body_xyz
        quat = np.array(euler2quat(*env_obj.body_rpy))
        pad = np.append(pos,quat)
        joints = np.array([])
        for j in env_obj.jdict:
            joints = np.append(joints,env_obj.jdict[j].current_position())
        joints = joints[0::2]
        remote_data = np.concatenate([pad]+[joints])
        if if_comm:
            conn.setqpos(remote_data)

        score += r
        frame += 1
        if if_render:
            env.render("human")

        freq_count += 1
