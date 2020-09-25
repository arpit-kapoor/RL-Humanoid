import gym
import numpy as np
import sys

import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='test.xml')

WIDTH = 0.01
HEIGHT = 0.1
SIZE = 5
FACTOR = 2
CLSZ = 0.1*FACTOR
LENGTH = SIZE*0.1*FACTOR

index = tree.find('worldbody')
geoms =[]
geoms.append(ET.Element('geom',pos="{} {} {}".format(0,LENGTH,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',pos="{} {} {}".format(0,-LENGTH,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT)))
geoms.append(ET.Element('geom',pos="{} {} {}".format(LENGTH,0,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT),euler="0 0 1.57"))
geoms.append(ET.Element('geom',pos="{} {} {}".format(-LENGTH,0,HEIGHT) ,size="{} {} {}".format(LENGTH,WIDTH,HEIGHT),euler="0 0 1.57"))
   
for j in range(SIZE):
    for i in range((SIZE-1)//2):
        geoms.append(ET.Element('geom',pos="{} {} {}".format(CLSZ*(2*i+1),2*CLSZ*(j-SIZE//2),HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT),euler="0 0 1.57"))
        geoms.append(ET.Element('geom',pos="{} {} {}".format(-CLSZ*(2*i+1),2*CLSZ*(j-SIZE//2),HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT),euler="0 0 1.57"))

for j in range(SIZE):
    for i in range((SIZE-1)//2):
        geoms.append(ET.Element('geom',pos="{} {} {}".format(2*CLSZ*(j-SIZE//2),CLSZ*(2*i+1),HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT)))
        geoms.append(ET.Element('geom',pos="{} {} {}".format(2*CLSZ*(j-SIZE//2),-CLSZ*(2*i+1),HEIGHT) ,size="{} {} {}".format(CLSZ,WIDTH,HEIGHT)))


for geom in geoms:
    index.append(geom)
tree.write('maze2.xml')
