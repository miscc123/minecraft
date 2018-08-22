# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:03:54 2018

@author: NTPU
"""


from mcpi.minecraft import Minecraft
import time
miscc123=Minecraft.create()
x,y,z=miscc123.player.getPos()
miscc123.setBlock(x,y,z,79)