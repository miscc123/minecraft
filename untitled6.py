# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:29:10 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
while True:
    x,y,z = miscc123.player.getPos()
    miscc123.setBlock(x,y,z,11)
    time.sleep(0.5)
