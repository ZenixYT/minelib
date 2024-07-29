from dataclasses import dataclass

@dataclass
class ItemComponent:
    component_name: str
    component_value: str | int | bool | float

    def get_mc_str(self):
        return f"{self.component_name}={str(self.component_value).lower()}"