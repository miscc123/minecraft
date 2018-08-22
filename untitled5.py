# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:29:01 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()

x,y,z=miscc123.player.getPos()

width = 10
length = 6
height = 5
block = 57
air = 0
while True:
    miscc123.setBlocks(x,y,z,x+width,y+height,z+length,block)
    miscc123.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air)