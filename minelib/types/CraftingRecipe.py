from dataclasses import dataclass
from minelib.types.ItemStack import ItemStack, ItemMeta

@dataclass
class CraftingKey:
    key: str
    item_id: str

@dataclass
class CraftingRecipe:
    recipe_name: str
    recipe_category: str
    is_recipe_shaped: bool
    item_crafted: ItemStack
    pattern: list[str]
    crafting_keys: list[CraftingKey]