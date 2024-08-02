from dataclasses import dataclass
from enum import Enum, auto

class TargetSelector(Enum):
    ALL = "@a"
    SELF = "@s"
    RANDOM = "@r"
    CLOSEST = "@p"
    ALL_ENTITIES = "@e"

class DistanceOps(Enum):
    EQUALS = auto()
    GREATER_THAN_OR_EQUAL_TO = auto()
    LESS_THAN_OR_EQUAL_TO = auto()
    GREATER_THAN = auto()
    LESS_THAN = auto()

class EntitySpecifier():
    def __init__(self, base_specifier: TargetSelector | str):
        self.base_specifier: TargetSelector | str = base_specifier.value if isinstance(base_specifier, TargetSelector) else base_specifier
        self.statements: list[str] = []

    def dx(self, dx: int):
        self.statements.append(f"dx={dx}")
        return self
    
    def dy(self, dy: int):
        self.statements.append(f"dy={dy}")
        return self
    
    def dz(self, dz: int):
        self.statements.append(f"dz={dz}")
        return self
    
    def tag(self, tag: str):
        self.statements.append(f"tag={tag}")
        return self
    
    def type(self, entity: str, not_: bool = False):
        self.statements.append(f"type={'!' if not_ else ''}{entity}")
        return self
    
    def limit(self, limit: int):
        self.statements.append(f"limit={limit}")
        return self
    
    def distance(self, distance: int, operator: DistanceOps):
        if operator == DistanceOps.EQUALS:
            self.statements.append(f"distance={distance}")
        elif operator == DistanceOps.GREATER_THAN:
            self.statements.append(f"distance={distance + 1}..")
        elif operator == DistanceOps.GREATER_THAN_OR_EQUAL_TO:
            self.statements.append(f"distance={distance}..")
        elif operator == DistanceOps.LESS_THAN:
            self.statements.append(f"distance=..{distance - 1}")
        elif operator == DistanceOps.LESS_THAN_OR_EQUAL_TO:
            self.statements.append(f"distance=..{distance}")
        return self

    def nbt(self, nbt: str):
        self.statements.append(f"nbt={nbt}")
        return self

    def to_string(self):
        statements_str = f'[{",".join(self.statements)}]' if len(self.statements) > 0 else ''
        return f"{self.base_specifier.value if isinstance(self.base_specifier, TargetSelector) else self.base_specifier}{statements_str}"