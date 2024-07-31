from dataclasses import dataclass
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.types.EntityTypesTag import EntityTypesTag

@dataclass
class EntitySpecifier():
    base_specifier: PlayerSpecifier
    statements: list[str] = []

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

    def to_string(self):
        return f'{self.base_specifier}[{','.join(self.statements)}]'