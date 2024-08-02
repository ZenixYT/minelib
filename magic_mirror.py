from minelib import *

pack = Pack("MagicMirror", "Zenn", 48)

item = ItemStack("minecraft:carrot_on_a_stick")
meta = item.get_item_meta()

meta.set_display_name("Magic Mirror")
meta.custom_model_data = 1001

item.set_item_meta(meta)

self_specifier = EntitySpecifier(TargetSelector.SELF)

@pack.load
def on_load():
    obj = pack.services.ScoreboardService.create_objective("used_coas", type_="minecraft.used:minecraft.carrot_on_a_stick")
    obj.set_score(0, EntitySpecifier(TargetSelector.ALL))

    pack.services.ScoreboardService.create_objective("BedSpawn")

@pack.function
def on_magic_mirror_used():
    bedObj = pack.services.ScoreboardService.get_objective("BedSpawn")

    Execute().as_(self_specifier).store_result_in_score(bedObj, EntitySpecifier("$bedX")).run_command("data get entity @s SpawnX")
    Execute().as_(self_specifier).store_result_in_score(bedObj, EntitySpecifier("$bedY")).run_command("data get entity @s SpawnY")
    Execute().as_(self_specifier).store_result_in_score(bedObj, EntitySpecifier("$bedZ")).run_command("data get entity @s SpawnZ")

    placeholder = Entity("minecraft:area_effect_cloud", Location(0, 10000, 0))
    placeholder.tags.append("MAGIC_MIRROR_REF")
    placeholder.spawn_entity()

    Execute().as_(placeholder.get_specifier()).store_result_in_entity(placeholder.get_specifier(), "Pos[0]", NBTType.DOUBLE).run_command("scoreboard players get $bedX BedSpawn")
    Execute().as_(placeholder.get_specifier()).store_result_in_entity(placeholder.get_specifier(), "Pos[1]", NBTType.DOUBLE).run_command("scoreboard players get $bedY BedSpawn")
    Execute().as_(placeholder.get_specifier()).store_result_in_entity(placeholder.get_specifier(), "Pos[2]", NBTType.DOUBLE).run_command("scoreboard players get $bedZ BedSpawn")

    pack.services.PlayerService.teleport_to_entity_or_player(self_specifier, placeholder.get_specifier())
    
    placeholder.kill_entity()

    bedObj.set_score(0, EntitySpecifier("$bedX"))
    bedObj.set_score(0, EntitySpecifier("$bedY"))
    bedObj.set_score(0, EntitySpecifier("$bedZ"))

@pack.tick
def on_tick():
    obj = pack.services.ScoreboardService.get_objective("used_coas")
    if obj is not None:
        Execute().as_(EntitySpecifier(TargetSelector.ALL)).if_score(obj, 1, ScoreMatchesOps.GREATER_THAN_OR_EQUAL_TO, EntitySpecifier(TargetSelector.SELF)).if_item_in_mainhand(item).run_function(on_magic_mirror_used)

        obj.set_score(0, EntitySpecifier(TargetSelector.ALL))
    
pack.dump()