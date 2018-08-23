# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:28 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
x,y,z = miscc123.player.getPos()
miscc123.cr(x,y,z,63)