# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:33:44 2018

@author: NTPU
"""
import time, random
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
pos = miscc123.player.getPos()
while True:
    x=pos.x+random.uniform(-50,50)
    y=pos.y+40
    z=pos.z++random.uniform(-50,50)
    miscc123.spawnEntity(x,y,z,63)
    time,sleep(0.1)