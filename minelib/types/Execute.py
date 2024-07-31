from minelib.types.Location import Location
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.types.EntitySpecifier import EntitySpecifier
from minelib.services.Scoreboard import Objective
from minelib.types.ItemStack import ItemStack
from enum import Enum, auto

class ScoreMatchesOps(Enum):
    EQUALS = auto()
    GREATER_THAN_OR_EQUAL_TO = auto()
    LESS_THAN_OR_EQUAL_TO = auto()
    GREATER_THAN = auto()
    LESS_THAN = auto()

class AnchorPosition(Enum):
    EYES = "eyes"
    FEET = "feet"

class Execute:
    def __init__(self):
        self.statements: list[str] = []
        self.player_or_entity: EntitySpecifier = None

    def as_(self, player_or_entity: EntitySpecifier):
        self.statements.append(f"as {player_or_entity.to_string()}")
        self.player_or_entity = player_or_entity
        return self

    def at(self, player_or_entity: EntitySpecifier):
        objPlr = player_or_entity if player_or_entity != None else self.player_or_entity
        self.statements.append(f"at {objPlr.to_string()}")
        return self

    def if_block(self, loc: Location, block_id: str):
        self.statements.append(f"if block {loc.X} {loc.Y} {loc.Z} {block_id}")
        return self
    
    def if_score(self, objective: Objective, score: int, operation: ScoreMatchesOps, entity: EntitySpecifier = None):
        objPlr: EntitySpecifier = entity if entity != None else self.player_or_entity
        if operation == ScoreMatchesOps.EQUALS:
            self.statements.append(f"if score {objPlr.to_string()} {objective.name} matches {score}")
        elif operation == ScoreMatchesOps.GREATER_THAN:
            self.statements.append(f"if score {objPlr.to_string()} {objective.name} matches {score + 1}..")
        elif operation == ScoreMatchesOps.GREATER_THAN_OR_EQUAL_TO:
            self.statements.append(f"if score {objPlr.to_string()} {objective.name} matches {score}..")
        elif operation == ScoreMatchesOps.LESS_THAN:
            self.statements.append(f"if score {objPlr.to_string()} {objective.name} matches ..{score - 1}")
        elif operation == ScoreMatchesOps.LESS_THAN_OR_EQUAL_TO:
            self.statements.append(f"if score {objPlr.to_string()} {objective.name} matches ..{score}")
        
        return self
    
    def if_item_in_mainhand(self, item: ItemStack):
        self.statements.append(f"if items entity {self.player_or_entity.value if isinstance(self.player_or_entity, PlayerSpecifier) else self.player_or_entity} weapon.mainhand {item.get_mc_str()}")
        return self
    
    def if_entity(self, entity: EntitySpecifier):
        self.statements.append(f"if entity {entity.to_string()}")
        return self
    
    def positioned(self, loc: Location):
        self.statements.append(f"positioned {loc.to_string()}")
        return self
    
    def anchored(self, position: AnchorPosition):
        self.statements.append(f"anchored {position.value}")
        return self

    def custom(self, custom_statement: str):
        self.statements.append(custom_statement)
        return self

    def run_function(self, func: str):
        self.statements.append(f"run function {func}")

        __mcf = get_current_mcf()
        __mcf.content.append(f"execute {' '.join(self.statements)}")
        set_current_mcf(__mcf)

    def run_command(self, cmd: str):
        self.statements.append(f"run {cmd}")

        __mcf = get_current_mcf()
        __mcf.content.append(f"execute {' '.join(self.statements)}")
        set_current_mcf(__mcf)