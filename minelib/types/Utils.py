from minelib.services.Scoreboard import Objective
from minelib.types.Core.EntitySpecifier import EntitySpecifier, TargetSelector
from minelib.types.World.Entity import Entity, Location
from minelib.types.Core.Execute import Execute
from minelib.Pack import Pack

class Utils:
    def __init__(self, pack: Pack):
        self.pack = pack