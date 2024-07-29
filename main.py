from minelib.minelib import *
import items

pack = Pack("test", "Zenn", 48)

@pack.load
def on_load():
    obj = pack.services.ScoreboardService.create_objective("COAS_RightClick", type="minecraft.used:minecraft.carrot_on_a_stick")
    obj.set_score(0, PlayerSpecifier.ALL)

@pack.function
def on_coas_right_click():
    obj = pack.services.ScoreboardService.get_objective("COAS_RightClick")
    if obj != None:
        obj.set_score(0, PlayerSpecifier.SELF)
        pack.services.PlayerService.print_to_player("Right-clicked on COAS!", PlayerSpecifier.SELF)

@pack.tick
def on_tick():
    obj = pack.services.ScoreboardService.get_objective("COAS_RightClick")
    pack.services.Minecraft.execute_if_score_greater_than_or_equal_to(PlayerSpecifier.ALL, obj, 1, f"{pack.namespace}:on_coas_right_click")

#pack.dump()
pack.dump("C:/Users/carve/AppData/Roaming/com.modrinth.theseus/profiles/Fabulously Optimized (1)/saves/New World22/datapacks")