# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:43:53 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
miscc123=Minecraft.create()
while True:
    hits = miscc123.events.pollProjectileHits()
    if len(hits)>0:
        h = hits[0]
        x,y,z = h.pos.x, h.pos.y, h.pos.z
        miscc123.createExplosion(x,y,z,150)