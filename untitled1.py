# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:33:10 2018

@author: NTP
"""
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
import time
x,y,z=miscc123.player.getPos()
while y<=1000:
    miscc123.setBlock(x,y-1,z,60)
    time.sleep(0.2)
    miscc123.setBlock(x+1,y-1,z,60)
    time.sleep(0.2)
    miscc123.setBlock(x+1+1,y-1,z,60)
    time.sleep(0.2)
    miscc123.setBlock(x+2,y-1,z-1,60)
    time.sleep(0.2)
    miscc123.setBlock(x+2,y-1,z-2,60)
    time.sleep(0.2)
    miscc123.setBlock(x+1,y-1,z-2,60)
    time.sleep(0.2)
    miscc123.setBlock(x,y-1,z-2,60)
    time.sleep(0.2)
    miscc123.setBlock(x,y-1,z-1,60)
    time.sleep(0.2)
    y = y+1




