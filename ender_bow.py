from minelib import *

pack = Pack("EnderBow", "Zenn", 48)

item = ItemStack("minecraft:bow")
meta = item.get_item_meta()

meta.set_display_name("Ender Bow")
meta.custom_model_data = 1001

item.set_item_meta(meta)

arrow_specifier = EntitySpecifier(TargetSelector.ALL_ENTITIES).type("minecraft:arrow").distance(3, DistanceOps.LESS_THAN_OR_EQUAL_TO).limit(1)

@pack.load
def on_load():
    obj = pack.services.ScoreboardService.create_objective("used_bow", type_="minecraft.used:minecraft.bow")
    obj.set_score(0, EntitySpecifier(TargetSelector.ALL))

@pack.function
def on_ender_bow_used():
    pack.services.PlayerService.ride_entity(EntitySpecifier(TargetSelector.SELF), arrow_specifier)

@pack.tick
def on_tick():
    obj = pack.services.ScoreboardService.get_objective("used_bow")
    if obj is not None:
        Execute().as_(EntitySpecifier(TargetSelector.ALL)).if_score(obj, 1, ScoreMatchesOps.GREATER_THAN_OR_EQUAL_TO, EntitySpecifier(TargetSelector.SELF)).run_function(on_ender_bow_used)

        obj.set_score(0, EntitySpecifier(TargetSelector.ALL))
    
pack.dump()