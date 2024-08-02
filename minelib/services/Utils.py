from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Core.EntitySpecifier import EntitySpecifier

class Utils:
    def __init__(self, pack):
        self.pack = pack

    def raycast(self, entity: EntitySpecifier, max_distance: int = 1000):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {entity.to_string()} run function {self.pack.namespace}lib:start_raycast")
        set_current_mcf(__mcf)