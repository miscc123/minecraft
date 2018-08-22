# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:36:13 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
x,y,z = miscc123.player.getPos()
a = 0
while a<20:
    miscc123.setBlocks(x+30,y-1,z,x-30,y-30,z,19)
    x = x-5
    a = a+1