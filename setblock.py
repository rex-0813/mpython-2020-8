
from mcpi.minecraft import Minecraft                        
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlock(x+1,y,z,20)
mc.setBlock(x-1,y,z,20)
mc.setBlock(x,y,z+1,20)
mc.setBlock(x,y,z-1,2)