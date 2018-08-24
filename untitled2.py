# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:23:51 2018

@author: NTPU
"""
from random import randrange
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
x,y,z = miscc123.player.getPos()
for i in range(20):
    r=randrange(1,6)
    c=randrange(15)
    l=randrange(2,16)
    if r==1:
        miscc123.setBlocks(x,y,z,x+l,y,z,35,c)
        x = x+4
    elif r==2:
        miscc123.setBlocks(x,y,z,x-l,y,z,35,c)
        x = x-4
    elif r==3:
        miscc123.setBlocks(x,y,z,x,y,z+l,35,c)
        z = z+4
    elif r==4:
        miscc123.setBlocks(x,y,z,x,y,z-l,35,c)
        z = z-4
    elif r==5:
        miscc123.setBlocks(x,y,z,x,y+l,z,35,c)
        y = y+4
    elif r==46:
        miscc123.setBlocks(x,y,z,x,y-l,z,35,c)
        y = y-4