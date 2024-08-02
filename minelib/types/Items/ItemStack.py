from dataclasses import dataclass
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Items.ItemMeta import ItemMeta
import json

class ItemStack:
    def __init__(self, item_id: str, count: int = 1):
        self.item_id = item_id
        self.count = count
        self.meta = ItemMeta()

    def get_item_meta(self):
        return self.meta

    def set_item_meta(self, meta: ItemMeta):
        self.meta = meta

    def get_mc_str(self):
        component_list: list[str] = []
        
        for component in self.get_item_meta().components:
            component_list.append(component.get_mc_str())

        if self.meta.display_name is not None:
            jSon = json.dumps(self.meta.display_name.dump())
            component_list.append(f"minecraft:item_name='{jSon}'")

        if self.meta.custom_model_data is not None:
            component_list.append(f"minecraft:custom_model_data={self.meta.custom_model_data}")

        return f"{self.item_id}[{','.join(component_list)}]"