# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:21:04 2018

@author: NTPU
"""
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
number = 1
x,y,z = miscc123.player.getPos()
for j in range(10)
    for i in range(number):
        miscc123.spawnEntity(x,y,z,60)
        
    number = number*2
    misc123.postToChat("恭喜妳生成了"+str(number)+"隻")