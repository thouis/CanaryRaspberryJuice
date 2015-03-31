A fork of the CanarRaspberryJuice plugin, optimized for large cuboid
editing and transfer.  This mod and python API should be able to
transfer fairly large cuboids of data, with different types and data
for each block in that cuboid, without causing undue lag.

TODO:
   * optimize server-> client cuboid transfer in the same way
   * add support for numpy array sending & receiving
   * Maybe: allow user to specify which of X,Y,Z to loop over when sending a block
   * Not by me: update Java client to match new API
   * Add Extra Features (see below)

Original README below..




-------------------------------------------------------------------------------
Raspberry Juice for Canarymod
Martin O'Hanlon (martin@ohanlonweb.com)
http://www.stuffaboutcode.com
-------------------------------------------------------------------------------

RaspberryJuice - A Canarymod plugin which implements the Minecraft Pi Socket API.

Migrated from the RaspberryJuice bukkit plugin. Original work by zhuowei

https://github.com/zhuowei/RaspberryJuice

http://dev.bukkit.org/bukkit-plugins/raspberryjuice/

Features currently supported:
 - world.get/setBlock
 - world.getBlockWithData
 - world.setBlocks
 - world.getPlayerIds
 - world.getBlocks
 - chat.post
 - events.clear
 - events.block.hits
 - player.getTile
 - player.setTile
 - player.getPos
 - player.setPos
 - world.getHeight
 - entity.getTile
 - entity.setTile
 - entity.getPos
 - entity.setPos

Features that can't be supported:
 - Camera angles

Extra features(**):
 - getBlocks(x1,y1,z1,x2,y2,z2) has been implemented
 - getDirection, getRotation, getPitch functions - get the 'direction' players and entities are facing
 - getPlayerId(playerName) - get the entity of a player by name
 - multiplayer support
   - name added as an option parameter to player.
   - modded minecraft.py in python api library so player "name" can be passed on Minecraft.create(ip, port, name)
   - this change does not stop standard python api library being used
 - the default tcp port can be changed in config/CanaryRaspberryJuicePlugin/CanaryRaspberryJuicePlugin.cfg

** to use the extra features an modded version of the java and python libraries that were originally supplied by Mojang with the Pi is required, https://github.com/martinohanlon/CanaryRaspberryJuice/tree/master/resources/mcpi.  You only need the modded libraries to use the extra features, the original libraries still work, you just wont be able to use the extra features

** please note extra features are NOT guaranteed to be maintained in future releases, particularly if updates are made to the original Pi API which replace the functionality

------------------------------------------------------------------------------

Version history
- 0.1 - Initial stable version
- 1.0 - First release.  Tested extensively with Canarymod 1.7.10-1.1.2
- 1.0.1 - Minor bug fix
- 1.0.2 - Recreated with Java 1.6
- 1.1 - Implemented entity functions
- 1.2 - added getPlayerId(playerName), getDirection, getRotation, getPitch

-------------------------------------------------------------------------------
