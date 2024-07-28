from enum import Enum
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.PlayerSpecifier import PlayerSpecifier

class ScoreboardOperationType(Enum):
    ADD = "+="
    SUBTRACT = "-="
    MULTIPLY = "*="
    DIVIDE = "/="
    MODULO = "%="
    # Need to add the rest later

class Objective:
    def __init__(self, name: str, displayName: str = "_", type: str = "dummy"):
        self.name = name
        self.displayName = displayName if displayName != "_" else name
        self.type = type

        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard objectives add {self.name} {self.type} "{self.displayName}"')
        set_current_mcf(_mcf)
    
    def set_score(self, new_score: int, destined_player: str | PlayerSpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players set {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {self.name} {new_score}')
        set_current_mcf(_mcf)

    def add_score(self, new_score: int, destined_player: str | PlayerSpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players add {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {self.name} {new_score}')
        set_current_mcf(_mcf)

    def remove_score(self, new_score: int, destined_player: str | PlayerSpecifier):
        _mcf = get_current_mcf()
        _mcf.content.append(f'scoreboard players remove {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {self.name} {new_score}')
        set_current_mcf(_mcf)

class Scoreboard:
    def __init__(self):
        self.objectives: list[Objective] = []

    def create_objective(self, name: str, displayName: str = "_", type: str = "dummy") -> Objective:
        new_obj = Objective(name, displayName, type)
        self.objectives.append(new_obj)
        return new_obj
    
    def get_objective(self, name: str) -> Objective | None:
        for obj in self.objectives:
            if obj.name == name:
                return obj
        return None