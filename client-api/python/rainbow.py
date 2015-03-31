import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 60

def sphere():
    count = 0
    for x in range(-64, 64):
        for y in range(-64, 64):
            for z in range(-64, 64):
                count = count + 1
                if (x*x + y*y + z*z < 64*64):
                    yield block.WOOL.id
                else:
                    yield block.AIR.id

def pattern():
    count = 0
    for x in range(-64, 64):
        for y in range(-64, 64):
            for z in range(-64, 64):
                count = count + 1
                if (x*x + y*y + z*z < 64*64):
                    count = count + 1
                    yield colors[count % len(colors)]
                else:
                    yield 0

mc.setBlocks(-40, -40, -40, 40, 100, 40, block.AIR.id)
mc.setBlocks(-64, 0, -64, 64 - 1, 128 - 1, 64 - 1, sphere(), pattern())

#for x in range(-256, 256):
#        for colourindex in range(0, len(colors)):
#                y = abs(sin((x / 128.0) * pi)) * height + colourindex
#                mc.setBlock(x - 64, y, 0, block.TNT.id)
