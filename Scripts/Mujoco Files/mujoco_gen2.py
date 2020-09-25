import gym
import gym_maze
import numpy as np
import sys

import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='test.xml')
env = gym.make('maze-sample-5x5-v0')

WIDTH = 0.05
HEIGHT = 0.5*2
SIZE = 5
FACTOR = 20
CLSZ = 0.1*FACTOR
LENGTH = SIZE*0.1*FACTOR

index = tree.find('worldbody')
geoms =[]
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(LENGTH,0,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(LENGTH,-2*LENGTH,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(0,-LENGTH,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(2*LENGTH,-LENGTH,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(CLSZ,-2*CLSZ,HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(2*CLSZ,-3*CLSZ,HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(2*CLSZ,-6*CLSZ,HEIGHT) ,size="{} {} {}".format(2*CLSZ,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(2*CLSZ,-9*CLSZ,HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(4*CLSZ,-5*CLSZ,HEIGHT) ,size="{} {} {}".format(3*CLSZ,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(6*CLSZ,-4*CLSZ,HEIGHT) ,size="{} {} {}".format(4*CLSZ,WIDTH,HEIGHT),euler="0 0 90"))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(7*CLSZ,-2*CLSZ,HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(8*CLSZ,-7*CLSZ,HEIGHT) ,size="{} {} {}".format(3*CLSZ,WIDTH,HEIGHT),euler="0 0 90"))

counter = 1
for geom in geoms:
    index.append(geom)
    tree_temp = ET.ElementTree(file='empty.xml')
    index_temp = tree_temp.find('worldbody')
    index_temp.append(geom)
    tree_temp.write("temp/maze_piece"+str(counter)+".xml")
    counter+=1 

tree.write('maze2.xml')