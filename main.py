from minelib.minelib import *

pack = Pack("EnderBow", "Zenn", 48)

ender_bow = ItemStack("minecraft:bow", 1)
ender_bow_meta = ender_bow.get_item_meta()

ender_bow_meta.set_display_name("Ender Bow")
ender_bow_meta.custom_model_data = 1001

ender_bow.set_item_meta(ender_bow_meta)

ender_bow_recipe = CraftingRecipe("ender_bow", "equipment", True, ender_bow, ["###", "#B#", "###"], [CraftingKey("#", "minecraft:ender_pearl"), CraftingKey("B", "minecraft:bow")])
pack.register_crafting_recipe(ender_bow_recipe)

@pack.load
def on_load():
    obj = pack.services.ScoreboardService.create_objective("Bow_RightClick", type="minecraft.used:minecraft.bow")
    obj.set_score(0, PlayerSpecifier.ALL)
    #pack.services.PlayerService.give_item(ender_bow, PlayerSpecifier.ALL)

@pack.function
def on_ender_bow_used():
    Execute().as_(PlayerSpecifier.SELF).at(PlayerSpecifier.SELF).run_command("ride @s mount @e[type=arrow, limit=1, distance=..3]")
    Execute().at(PlayerSpecifier.SELF).as_("@e[type=arrow, limit=1, distance=..3]").run_command("effect give @s minecraft:invisibility infinite 255 true")

@pack.function
def on_bow_used():
    obj = pack.services.ScoreboardService.get_objective("Bow_RightClick")
    if obj != None:
        Execute().as_(PlayerSpecifier.SELF).if_item_in_mainhand(ender_bow).run_function(f"{pack.namespace}:on_ender_bow_used")
        obj.set_score(0, PlayerSpecifier.SELF)

@pack.tick
def on_tick():
    obj = pack.services.ScoreboardService.get_objective("Bow_RightClick")
    if obj != None:
        Execute().as_(PlayerSpecifier.ALL).if_score(obj, 1, ScoreMatchesOps.GREATER_THAN_OR_EQUAL_TO, player_or_entity=PlayerSpecifier.SELF).run_function(f"{pack.namespace}:on_bow_used")

pack.dump()