from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.services.Scoreboard import Objective
from minelib.types.Core.EntitySpecifier import EntitySpecifier, TargetSelector
from minelib.types.Core.NBT import NBTCompound, NBTType
from minelib.types.World.Entity import Entity, Location
from minelib.types.Core.Execute import Execute
#from minelib.Pack import Pack # Only for debugging

class Utils:
    def __init__(self, pack):
        self.pack = pack

    def raycast(self, entity: EntitySpecifier, max_distance: int = 1000):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {entity.to_string()} run function {self.pack.namespace}lib:start_raycast")
        set_current_mcf(__mcf)

    def generate_random_number_and_store_to_score(self, objective: Objective, player: EntitySpecifier, max: int = -1):
        aac = Entity("minecraft:area_effect_cloud", Location(0, 10000, 0))
        aac.tags.append("ML_RANDOM_NUMBER")
        aac.spawn_entity()

        Execute().store_result_in_score(objective, player).run_command(f"data get entity {aac.get_specifier()} UUID[0] 1")

        #TODO: Implement range

        aac.kill_entity()

    def shoot_from_entity_facing(self, src_entity: EntitySpecifier, entity_to_spawn: Entity):
        marker = Entity("minecraft:marker", Location(0, 0, 1, True, True))
        marker.tags.append("MINELIB_SHOOT_FROM_ENTITY_FACING_DIRECTION")
        marker.spawn_entity()

        obj = self.pack.services.ScoreboardService.create_objective("minelibshootfacing")

        Execute().store_result_in_score(obj, EntitySpecifier("$playerX")).run_command("data get entity @s Pos[0] 1000")
        Execute().store_result_in_score(obj, EntitySpecifier("$playerY")).run_command("data get entity @s Pos[1] 1000")
        Execute().store_result_in_score(obj, EntitySpecifier("$playerZ")).run_command("data get entity @s Pos[2] 1000")
        
        Execute().store_result_in_score(obj, EntitySpecifier("$targetX")).as_(marker.get_specifier().limit(1)).run_command("data get entity @s Pos[0] 1000")
        Execute().store_result_in_score(obj, EntitySpecifier("$targetY")).as_(marker.get_specifier().limit(1)).run_command("data get entity @s Pos[1] 1000")
        Execute().store_result_in_score(obj, EntitySpecifier("$targetZ")).as_(marker.get_specifier().limit(1)).run_command("data get entity @s Pos[2] 1000")

        Execute().run_command(f"scoreboard players operation $targetX {obj.name} -= $playerX {obj.name}")
        Execute().run_command(f"scoreboard players operation $targetY {obj.name} -= $playerY {obj.name}")
        Execute().run_command(f"scoreboard players operation $targetZ {obj.name} -= $playerZ {obj.name}")

        entity_to_spawn.tags.append("MINELIB_SHOOT_FACING_SPAWNED")
        entity_to_spawn.spawn_entity()

        Execute().store_result_in_entity(entity_to_spawn.get_specifier(), "Motion[0]", NBTType.DOUBLE, 0.001).run_command(f"scoreboard players get $targetX {obj.name}")
        Execute().store_result_in_entity(entity_to_spawn.get_specifier(), "Motion[1]", NBTType.DOUBLE, 0.001).run_command(f"scoreboard players get $targetY {obj.name}")
        Execute().store_result_in_entity(entity_to_spawn.get_specifier(), "Motion[2]", NBTType.DOUBLE, 0.001).run_command(f"scoreboard players get $targetZ {obj.name}")
        
        self.pack.services.PlayerService.remove_tags(entity_to_spawn.get_specifier(), "MINELIB_SHOOT_FACING_SPAWNED")

        marker.kill_entity()