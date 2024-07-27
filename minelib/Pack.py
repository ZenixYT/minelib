from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.PlayerSpecifier import PlayerSpecifier

from minelib.services.Player import Player
from minelib.services.Server import Server
from minelib.services.World import World

import os, json

class Services:
    def __init__(self):
        self.PlayerService = Player()
        self.ServerService = Server()
        self.WorldService = World()

class Pack():
    def __init__(self, name: str, author: str, version: str):
        self.name = name
        self.namespace = name.lower()
        self.author = author
        self.version = version
        
        self.load_funcs: list[mcfunction] = []
        self.tick_funcs: list[mcfunction] = []
        self.funcs: list[mcfunction] = []

        self.services = Services()

    # Decorators
    def function(self, func):
        mcf = mcfunction(func.__name__)
        set_current_mcf(mcf)
        func()
        set_current_mcf(None)
        self.funcs.append(mcf)
        return mcf
    
    def tick(self, func):
        mcf = self.function(func)
        self.tick_funcs.append(mcf)
    
    def load(self, func):
        mcf = self.function(func)
        self.load_funcs.append(mcf)
    
    def run_function(self, funcName, destinedPlayer: PlayerSpecifier = PlayerSpecifier.SELF):
        mcf: mcfunction = None
        for func in self.funcs:
            if func.name == funcName:
                mcf = func
        if mcf is not None:
            __mcf = get_current_mcf()
            __mcf.content.append(f"execute as {destinedPlayer.value} run function {self.namespace}:{mcf.name}")
            set_current_mcf(__mcf)

    def dump(self):
        pack_mcmeta = {
            "pack": {
                "pack_format": self.version,
                "description": "Generated with minelib!"
            }
        }

        os.makedirs(f"{self.name}/data/{self.namespace}/functions", exist_ok=True)
        with open(f"{self.name}/pack.mcmeta", 'w') as pack_mcmeta_file:
            json.dump(pack_mcmeta, pack_mcmeta_file, indent=4)
        
        for i in self.funcs:
            with open(f"{self.name}/data/{self.namespace}/functions/{i.name}.mcfunction", 'w') as f:
                f.write("\n".join(i.content))