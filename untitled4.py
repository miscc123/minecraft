# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:14:03 2018

@author: NTPU
"""

from random import randrange
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()

for j in range(50):
    x,y,z = miscc123.player.getPos()
    x = x+j
    for i in range(50):
        r = randrange(16)
        miscc123.setBlock(x,y,z,35,r)
        z = z+1
r = randrange(0,16)
while True:
     hits = miscc123.events.pollBlockHits()
     if len(hits)>0:
         h = hits[0]
         block = miscc123.getBlockWithData(h.pos)
         data = block.data
         if data==r:
             miscc123.postToChat("找到囉")
             miscc123.setBlock(h.pos,57)
             break
         elif data>r:
             miscc123.postToChat("要找更小的方塊")
         elif data<r:
             miscc123.postToChat("要找更大的方塊")