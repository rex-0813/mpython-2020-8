# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:25:44 2020

@author: USER
"""

from mcpi.minecraft import Minecraft                        
mc = Minecraft.create()

print(mc.player.getTilePos())
