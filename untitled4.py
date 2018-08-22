# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:01:35 2018

@author: NTPU
"""
import random,time
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()

while True:
    x,y,z=miscc123.player.getPos()
    color = random.randrange(1,16)
    miscc123.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)
    time.sleep(1)