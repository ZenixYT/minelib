from dataclasses import dataclass
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Core.Location import Location
from minelib.types.Core.EntitySpecifier import EntitySpecifier, TargetSelector
import json

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

    def __init__(self, entity_id: str, loc: Location):
        self.entity_id: str = entity_id
        self.loc: Location = loc
        self.tags: list[str] = []
        self.motion: Location = None
        self.no_ai: bool = False
        self.no_gravity: bool = False
        self.silent: bool = False
        self.fire_ticks: int = 0
        self.invulnerable: bool = False
        self.health: float = -1.0
        self.spawned: bool = False

    def synthesize_nbt(self):
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

        return json.dumps(nbt)

    def spawn_entity(self) -> EntitySpecifier:
        nbt = self.synthesize_nbt()

        __mcf = get_current_mcf()
        __mcf.content.append(f"summon {self.entity_id} {self.loc.to_string()} {nbt}")
        set_current_mcf(__mcf)

        self.spawned = True
    
    def kill_entity(self):
        if self.spawned:
            __mcf = get_current_mcf()
            __mcf.content.append(f"kill {self.get_specifier().to_string()}")
            set_current_mcf(__mcf)

    def get_specifier(self) -> EntitySpecifier | None:
        new_spec = EntitySpecifier(TargetSelector.ALL_ENTITIES).nbt(self.synthesize_nbt())
        return new_spec if self.spawned else None