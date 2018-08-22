# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:47:41 2018

@author: NTPU
"""
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
x,y,z = miscc123.player.getPos()
a=miscc123.getBlock(x+1,y-1,z)
b=miscc123.getBlock(x-1,y-1,z)
c=miscc123.getBlock(x,y-1,z+1)
d=miscc123.getBlock(x,y-1,z+1)
if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
    miscc123.setBlocks(z+1,y-1,z+1,x-1,y-1,z-1,103)