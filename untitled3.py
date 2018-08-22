# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:15:24 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()

x,y,z=miscc123.player.getPos()
#miscc123.player.setPos(x+0.5,y,z+0.5)
miscc123.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,11)