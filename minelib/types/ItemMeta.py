from dataclasses import dataclass
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf

@dataclass
class ItemMeta:
    display_name: str = None
    custom_model_data: int = None

    def has_custom_model_data(self):
        return True if self.custom_model_data is not None else False
    
    def get_custom_model_data(self):
        return self.custom_model_data

    def set_custom_model_data(self, custom_model_data: int):
        self.custom_model_data = custom_model_data

    def get_display_name(self):
        return self.display_name
    
    def set_display_name(self, name: str):
        self.display_name = name