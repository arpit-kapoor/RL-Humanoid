import gym
import gym_maze
import numpy as np
import sys

import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='test.xml')
env = gym.make('maze-sample-5x5-v0')

WIDTH = 0.1
HEIGHT = 1
SIZE = 5
FACTOR = 15
CLSZ = 0.1*FACTOR
LENGTH = SIZE*0.1*FACTOR

index = tree.find('worldbody')
geoms =[]
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+LENGTH,0+CLSZ,HEIGHT) ,size="{} {} {}".format(2*LENGTH,WIDTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+LENGTH,-2*LENGTH+CLSZ,HEIGHT) ,size="{} {} {}".format(2*LENGTH,WIDTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+0,-LENGTH+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,2*LENGTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+2*LENGTH,-LENGTH+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,2*LENGTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+CLSZ,-2*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(2*CLSZ,WIDTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+2*CLSZ,-3*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,2*CLSZ,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+2*CLSZ,-6*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(4*CLSZ,WIDTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+2*CLSZ,-9*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,2*CLSZ,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+4*CLSZ,-5*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,6*CLSZ,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+6*CLSZ,-4*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,8*CLSZ,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+7*CLSZ,-2*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(2*CLSZ,WIDTH,2*HEIGHT)))
geoms.append(ET.Element('geom',type="box",rgba="0.2 0.6 1 1",pos="{} {} {}".format(-CLSZ+8*CLSZ,-7*CLSZ+CLSZ,HEIGHT) ,size="{} {} {}".format(WIDTH,6*CLSZ,2*HEIGHT)))

counter = 1
for geom in geoms:
    index.append(geom)
    tree_temp = ET.ElementTree(file='empty.xml')
    index_temp = tree_temp.find('worldbody')
    index_temp.append(geom)
    tree_temp.write("temp/maze_piece"+str(counter)+".xml")
    counter+=1 

tree.write('maze2.xml')