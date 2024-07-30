from dataclasses import dataclass
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Location import Location
import json

@dataclass
class Entity:
    entity_id: str
    loc: Location
    tags: list[str] = []

    def spawn_entity(self):
        nbt = {}
        if len(self.tags) > 0:
            nbt.update({"Tags": self.tags})

        __mcf = get_current_mcf()
        __mcf.content.append(f"summon {self.entity_id} {self.loc.to_string()} {json.dumps(nbt)}")
        set_current_mcf(__mcf)