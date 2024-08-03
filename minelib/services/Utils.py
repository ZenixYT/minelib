from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.services.Scoreboard import Objective
from minelib.types.Core.EntitySpecifier import EntitySpecifier, TargetSelector
from minelib.types.World.Entity import Entity, Location
from minelib.types.Core.Execute import Execute

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