# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:18:00 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
x,y,z = miscc123.player.getPos()
miscc123.setSign(x,y,z,63,0,"Hellow","","hi","")