from dataclasses import dataclass
from enum import Enum

class NBTType(Enum):
    INT = "int"
    FLOAT = "float"
    SHORT = "short"
    LONG = "long"
    DOUBLE = "double"
    BYTE = "byte"

class NBTCompound:
    name: str
    type_: NBTType
    value: any