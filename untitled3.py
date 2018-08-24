# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:18:23 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
while True:
    miscc123.executeCommand("time add 10")
    time.sleep(0.01)