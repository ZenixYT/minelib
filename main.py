from minelib.minelib import *

pack = Pack("test", "Zenn", 48)

@pack.tick
def on_tick():
    pack.services.WorldService.set_block_relative(PlayerSpecifier.ALL, Location(0, -1, 0), "minecraft:stone")

@pack.load
def on_load():
    pack.services.PlayerService.print_to_player("haii :3", PlayerSpecifier.ALL)

pack.dump("C:/Users/carve/AppData/Roaming/com.modrinth.theseus/profiles/Fabulously Optimized (1)/saves/New World22/datapacks")