# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:43:23 2018

@author: NTPU
"""


from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
list2 = [[57,41,14],
         [35,73,86]]
myid = miscc123.getPlayerEntityId("miscc123")
x,y,z=miscc123.entity.getTilePos(myid)
startx = x
for list1 in list2:
    for i in list1:
        miscc123.setBlock(x,y,z,i)
        x = x+1
    x=startx
    z=z+1
list2 = [[1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,10,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1]]