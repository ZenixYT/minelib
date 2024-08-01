from dataclasses import dataclass
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Location import Location
import json

@dataclass
class Entity:
    entity_id: str
    loc: Location
    tags: list[str] = []
    motion: Location = None
    no_ai: bool = False
    no_gravity: bool = False
    silent: bool = False
    fire_ticks: int = 0
    invulnerable: bool = False
    health: float = -1.0

    def spawn_entity(self):
        nbt = {}
        if len(self.tags) > 0:
            nbt.update({"Tags": self.tags})
        if self.motion is not None:
            nbt.update({"Motion": [float(self.motion.X), float(self.motion.Y), float(self.motion.Z)]})
        if self.no_ai:
            nbt.update({"NoAI": self.no_ai})
        if self.no_gravity:
            nbt.update({"NoGravity": self.no_gravity})
        if self.silent:
            nbt.update({"Silent": self.silent})
        if self.invulnerable:
            nbt.update({"Invulnerable": self.invulnerable})
        if self.health > -1:
            nbt.update({"Health": self.health})
        if self.fire_ticks > 0:
            nbt.update({"Fire": self.fire_ticks})

        __mcf = get_current_mcf()
        __mcf.content.append(f"summon {self.entity_id} {self.loc.to_string()} {json.dumps(nbt)}")
        set_current_mcf(__mcf)