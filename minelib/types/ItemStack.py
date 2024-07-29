from dataclasses import dataclass
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.ItemMeta import ItemMeta

class ItemStack:
    def __init__(self, item_id: str, count: int):
        self.item_id = item_id
        self.count = count
        self.meta = ItemMeta()

    def get_item_meta(self):
        return self.meta

    def set_item_meta(self, meta: ItemMeta):
        self.meta = meta