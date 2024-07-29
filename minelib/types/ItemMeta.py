from dataclasses import dataclass
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.ItemComponent import ItemComponent

class ItemMeta:
    def __init__(self):
        self.components: list[ItemComponent] = []

    def new_component(self, component: ItemComponent):
        self.components.append(component)

    def remove_component(self, component_name: str):
        for component in self.components:
            if component.component_name == component_name:
                self.components.remove(component)
                return
    
    def get_component(self, component_name: str):
        for component in self.components:
            if component.component_name == component_name:
                return component