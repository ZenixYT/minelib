from enum import Enum
from dataclasses import dataclass
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.Core.EntitySpecifier import EntitySpecifier

class ScoreboardOperationType(Enum):
    ADD = "+="
    SUBTRACT = "-="
    MULTIPLY = "*="
    DIVIDE = "/="
    MODULO = "%="
    # Need to add the rest later

class Objective:
    def __init__(self, name: str, displayName: str = "_", type: str = "dummy", create_objective: bool = True):
        self.name = name
        self.displayName = displayName if displayName != "_" else name
        self.type = type

        if create_objective:
            _mcf = get_current_mcf()
            _mcf.content.append(f'scoreboard objectives add {self.name} {self.type} "{self.displayName}"')
            set_current_mcf(_mcf)
    
    def set_score(self, new_score: int, player: EntitySpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players set {player.to_string()} {self.name} {new_score}')
        set_current_mcf(_mcf)

    def add_score(self, new_score: int, player: EntitySpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players add {player.to_string()} {self.name} {new_score}')
        set_current_mcf(_mcf)

    def remove_score(self, new_score: int, player: EntitySpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players remove {player.to_string()} {self.name} {new_score}')
        set_current_mcf(_mcf)

@dataclass
class Score:
    objective: Objective
    entity: EntitySpecifier

    def set_score(self, new_score: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f'scoreboard players set {self.entity.to_string()} {self.objective.name} {new_score}')
        set_current_mcf(__mcf)

    def add_score(self, new_score: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f'scoreboard players add {self.entity.to_string()} {self.objective.name} {new_score}')
        set_current_mcf(__mcf)
    
    def remove_score(self, new_score: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f'scoreboard players remove {self.entity.to_string()} {self.objective.name} {new_score}')
        set_current_mcf(__mcf)

class Scoreboard:
    def __init__(self):
        self.objectives: list[Objective] = []

    def create_objective(self, name: str, displayName: str = "_", type_: str = "dummy") -> Objective:
        new_obj = Objective(name, displayName, type_)
        self.objectives.append(new_obj)
        return new_obj
    
    def get_objective(self, name: str, already_exists_or_in_other_pack: bool = False) -> Objective | None:
        if already_exists_or_in_other_pack:
            return Objective(name, create_objective=False)
        else:
            for obj in self.objectives:
                if obj.name == name:
                    return obj
            return None