# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:21:15 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
myid = miscc123.getPlayerEntityId("miscc123")
miscc123.postToTitle(myid,"§Ahellow")