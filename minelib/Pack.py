from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.PlayerSpecifier import PlayerSpecifier

from minelib.services.Player import Player
from minelib.services.Server import Server
from minelib.services.World import World
from minelib.services.Scoreboard import Scoreboard, Objective
from minelib.services.Minecraft import Minecraft

import os, json

class Services:
    def __init__(self, pack):
        self.PlayerService = Player()
        self.ServerService = Server()
        self.WorldService = World()
        self.ScoreboardService = Scoreboard()
        self.Minecraft = Minecraft(pack)

class Pack():
    def __init__(self, name: str, author: str, version: str):
        self.name = name
        self.namespace = name.lower()
        self.author = author
        self.version = version
        
        self.load_funcs: list[mcfunction] = []
        self.tick_funcs: list[mcfunction] = []
        self.funcs: list[mcfunction] = []

        self.services = Services(self)

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
        return mcf
    
    def load(self, func):
        mcf = self.function(func)
        self.load_funcs.append(mcf)
        return mcf
    
    def run_function(self, funcName, destinedPlayer: PlayerSpecifier = PlayerSpecifier.SELF):
        mcf: mcfunction = None
        for func in self.funcs:
            if func.name == funcName:
                mcf = func
        if mcf is not None:
            __mcf = get_current_mcf()
            __mcf.content.append(f"execute as {destinedPlayer.value} run function {self.namespace}:{mcf.name}")
            set_current_mcf(__mcf)

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