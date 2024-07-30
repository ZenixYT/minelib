from dataclasses import dataclass

@dataclass
class ItemComponent:
    component_name: str
    component_value: str | int | bool | float

    def get_mc_str(self, remove_apostrophe: bool = False):
        return f"{self.component_name}={str(self.component_value).lower() if not isinstance(self.component_name, str) else self.component_value}"