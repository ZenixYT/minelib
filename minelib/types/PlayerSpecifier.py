from enum import Enum

class PlayerSpecifier(Enum):
    ALL = "@a"
    SELF = "@s"
    RANDOM = "@r"
    CLOSEST = "@p"