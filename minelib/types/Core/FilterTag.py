from dataclasses import dataclass

@dataclass
class FilterTag:
    name: str
    values: list[str]
    replace: bool