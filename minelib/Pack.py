from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf

from minelib.types.Core.EntitySpecifier import EntitySpecifier
from minelib.types.Items.ItemStack import ItemStack, ItemMeta
from minelib.types.Core.CraftingRecipe import CraftingRecipe, CraftingKey
from minelib.types.Core.FilterTag import FilterTag

from minelib.services.Player import Player
from minelib.services.Server import Server
from minelib.services.World import World
from minelib.services.Scoreboard import Scoreboard, Objective

import os, json

class Services:
    def __init__(self, pack):
        self.PlayerService = Player()
        self.ServerService = Server()
        self.WorldService = World()
        self.ScoreboardService = Scoreboard()

class Pack():
    def __init__(self, name: str, author: str, version: str, namespace: str = None, description: str = None):
        self.name = name
        self.namespace = name.lower() if namespace is None else namespace
        self.author = author
        self.version = version
        
        self.description = description if description is not None else f"Created by {self.author}; Generated with minelib!"
        
        self.load_funcs: list[mcfunction] = []
        self.tick_funcs: list[mcfunction] = []
        self.funcs: list[mcfunction] = []

        self.recipes: list[CraftingRecipe] = []
        self.entity_filters: list[FilterTag] = []
        self.block_filters: list[FilterTag] = []

        self.services = Services(self)

    # Decorators
    def function(self, func):
        mcf = mcfunction(func.__name__, self)
        set_current_mcf(mcf)
        func()
        set_current_mcf(None)
        self.funcs.append(mcf)
        return mcf
    
    def tick(self, func):
        mcf = self.function(func)
        self.tick_funcs.append(mcf)
        return mcf
    
    def load(self, func):
        mcf = self.function(func)
        self.load_funcs.append(mcf)
        return mcf
    
    def run_function(self, funcName, destinedPlayer: EntitySpecifier):
        mcf: mcfunction = None
        for func in self.funcs:
            if func.name == funcName:
                mcf = func
        if mcf is not None:
            __mcf = get_current_mcf()
            __mcf.content.append(f"execute as {destinedPlayer.to_string()} run function {self.namespace}:{mcf.name}")
            set_current_mcf(__mcf)

    def register_crafting_recipe(self, new_recipe: CraftingRecipe):
        self.recipes.append(new_recipe)

    def register_entity_type_filter(self, name: str, entities: list[str], replace: bool = False):
        new_tag = FilterTag(name, entities, replace)
        self.entity_filters.append(new_tag)

    def register_block_type_filter(self, name: str, blocks: list[str]):
        new_tag = FilterTag(name, blocks, False)
        self.block_filters.append(new_tag)

    def create_lib(self, path: str = "."):
        os.makedirs(f"{path}/{self.name}/data/{self.namespace}lib/function", exist_ok=True)

        

    def dump(self, path: str = "."):
        pack_mcmeta = {
            "pack": {
                "pack_format": self.version,
                "description": f"Created by {self.author}; Generated with minelib!"
            }
        }

        os.makedirs(f"{path}/{self.name}/data/{self.namespace}/function", exist_ok=True)
        os.makedirs(f"{path}/{self.name}/data/minecraft/tags/function", exist_ok=True)
        with open(f"{path}/{self.name}/pack.mcmeta", 'w') as pack_mcmeta_file:
            json.dump(pack_mcmeta, pack_mcmeta_file, indent=4)
        
        for i in self.funcs:
            with open(f"{path}/{self.name}/data/{self.namespace}/function/{i.name}.mcfunction", 'w') as f:
                f.write("\n".join(i.content))

        tickfuncs: list[str] = []
        for func in self.tick_funcs:
            tickfuncs.append(f"{self.namespace}:{func.name}")
        tick_json = {
            "values": tickfuncs
        }

        loadfuncs: list[str] = []
        for func in self.load_funcs:
            loadfuncs.append(f"{self.namespace}:{func.name}")
        load_json = {
            "values": loadfuncs
        } 

        with open(f"{path}/{self.name}/data/minecraft/tags/function/load.json", "w") as f:
            json.dump(load_json, f, indent = 4)

        with open(f"{path}/{self.name}/data/minecraft/tags/function/tick.json", "w") as f:
            json.dump(tick_json, f, indent = 4)

        if len(self.recipes) > 0:
            os.makedirs(f"{path}/{self.name}/data/{self.namespace}/recipe/", exist_ok=True)

            for recipe in self.recipes:
                key_json = {}
                for key in recipe.crafting_keys:
                    key_json.update({key.key: {"item": key.item_id}})
                
                components_json = {}
                item_crafted_meta = recipe.item_crafted.get_item_meta()
                for component in item_crafted_meta.components:
                    if isinstance(component.component_value, str):
                        components_json.update({component.component_name: component.component_value})
                    else:
                        components_json.update({component.component_name: component.component_value})

                if item_crafted_meta.display_name is not None:
                    jon = json.dumps(item_crafted_meta.display_name.dump())
                    components_json.update({"minecraft:item_name": jon})

                if item_crafted_meta.custom_model_data is not None:
                    components_json.update({"minecraft:custom_model_data": item_crafted_meta.custom_model_data})

                recipe_json = {
                    "type": f"{'minecraft:crafting_shaped' if recipe.is_recipe_shaped else 'minecraft:crafting_shapeless'}",
                    "category": recipe.recipe_category,
                    "pattern": recipe.pattern,
                    "key": key_json,
                    "result": {
                        "id": recipe.item_crafted.item_id,
                        "components": components_json
                    }
                }

                with open(f"{path}/{self.name}/data/{self.namespace}/recipe/{recipe.recipe_name}.json", "w") as f:
                    json.dump(recipe_json, f, indent = 4)