import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()

radius = 50

def sphere():
    count = 0
    for x in range(-radius, radius):
        for y in range(-radius, radius):
            for z in range(-radius, radius):
                count = count + 1
                if (x*x + y*y + z*z < radius*radius):
                    yield block.WOOL.id
                else:
                    yield block.AIR.id

def pattern():
    count = 0
    for x in range(-radius, radius):
        for y in range(-radius, radius):
            for z in range(-radius, radius):
                count = count + 1
                if (x*x + y*y + z*z < radius*radius):
                    count = count + 1
                    yield colors[count % len(colors)]
                else:
                    yield 0

mc.setBlocks(-radius, 0, -radius, radius - 1, 2 * radius - 1, radius - 1, sphere(), pattern())
