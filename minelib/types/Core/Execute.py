from minelib.types.Core.Location import Location
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Core.EntitySpecifier import EntitySpecifier
from minelib.services.Scoreboard import Objective
from minelib.types.Items.ItemStack import ItemStack
from minelib.types.Core.NBT import NBTCompound, NBTType
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

    def if_block(self, loc: Location, block_id: str, unless: bool = False):
        self.statements.append(f"{'if' if not unless else 'unless'} block {loc.X} {loc.Y} {loc.Z} {block_id}")
        return self
    
    def if_score(self, objective: Objective, score: int, operation: ScoreMatchesOps, entity: EntitySpecifier = None, unless: bool = False):
        objPlr: EntitySpecifier = entity if entity != None else self.player_or_entity
        if operation == ScoreMatchesOps.EQUALS:
            self.statements.append(f"{'if' if not unless else 'unless'} score {objPlr.to_string()} {objective.name} matches {score}")
        elif operation == ScoreMatchesOps.GREATER_THAN:
            self.statements.append(f"{'if' if not unless else 'unless'} score {objPlr.to_string()} {objective.name} matches {score + 1}..")
        elif operation == ScoreMatchesOps.GREATER_THAN_OR_EQUAL_TO:
            self.statements.append(f"{'if' if not unless else 'unless'} score {objPlr.to_string()} {objective.name} matches {score}..")
        elif operation == ScoreMatchesOps.LESS_THAN:
            self.statements.append(f"{'if' if not unless else 'unless'} score {objPlr.to_string()} {objective.name} matches ..{score - 1}")
        elif operation == ScoreMatchesOps.LESS_THAN_OR_EQUAL_TO:
            self.statements.append(f"{'if' if not unless else 'unless'} score {objPlr.to_string()} {objective.name} matches ..{score}")
        
        return self
    
    def if_item_in_mainhand(self, item: ItemStack, unless: bool = False):
        self.statements.append(f"{'if' if not unless else 'unless'} items entity {self.player_or_entity.to_string()} weapon.mainhand {item.get_mc_str()}")
        return self
    
    def if_entity(self, entity: EntitySpecifier, unless: bool = False):
        self.statements.append(f"{'if' if not unless else 'unless'} entity {entity.to_string()}")
        return self
    
    def positioned(self, loc: Location):
        self.statements.append(f"positioned {loc.to_string()}")
        return self
    
    def anchored(self, position: AnchorPosition):
        self.statements.append(f"anchored {position.value}")
        return self
    
    def store_result_in_score(self, objective: Objective, player: EntitySpecifier):
        self.statements.append(f"store result score {player.to_string()} {objective.name}")
        return self
    
    def store_result_in_entity(self, destination: EntitySpecifier, path: str, type_: NBTType, scale: int = 1):
        self.statements.append(f"store result entity {destination.to_string()} {path} {type_.value} {scale}")
        return self
    
    def store_result_in_storage(self, target: str, path: str, type_: NBTType, scale: int = 1):
        self.statements.append(f"store result storage {target} {path} {type_.value} {scale}")
        return self
    
    def store_result_in_block(self, loc: Location, path: str, type_: NBTType, scale: int = 1):
        self.statements.append(f"store result block {loc.to_string()} {path} {type_.value} {scale}")
        return self
    
    def store_result_in_bossbar(self):
        pass #TODO: Implement bossbars

    def in_dimension(self, dimension_id: str):
        self.statements.append(f"in {dimension_id}")
        return self
    
    def align(self, axes: str):
        self.statements.append(f"align {axes}")
        return self
    
    def facing(self, location: Location):
        self.statements.append(f"facing {location.to_string()}")
        return self
    
    def facing_entity(self, entity: EntitySpecifier, anchor: AnchorPosition):
        self.statements.append(f"facing entity {entity.to_string} {anchor.value}")
        return self
    
    def rotated(self, x: int, y: int):
        self.statements.append(f"rotated {x} {y}")
        return self

    def custom(self, custom_statement: str):
        self.statements.append(custom_statement)
        return self

    def run_function(self, func: mcfunction):
        self.statements.append(f"run function {func.function_name}")

        __mcf = get_current_mcf()
        __mcf.content.append(f"execute {' '.join(self.statements)}")
        set_current_mcf(__mcf)

    def run_command(self, cmd: str):
        self.statements.append(f"run {cmd}")

        __mcf = get_current_mcf()
        __mcf.content.append(f"execute {' '.join(self.statements)}")
        set_current_mcf(__mcf)