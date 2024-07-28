from minelib.types.Location import Location
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.PlayerSpecifier import PlayerSpecifier

class Minecraft:
    def __init__(self, pack):
        self.pack = pack

    def execute_if_block(self, loc: Location, block_id: str, func: str):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute if block {loc.X} {loc.Y} {loc.Z} {block_id} run function {func}")
        set_current_mcf(__mcf)
    
    def execute_if_block_relative_to_player(self, player: str | PlayerSpecifier, loc: Location, block_id: str, func: str):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.value if isinstance(player, PlayerSpecifier) else player} if block ~{loc.X if loc.X != 0 else ''} ~{loc.Y if loc.Y != 0 else ''} ~{loc.Z if loc.Z != 0 else ''} {block_id} run function {func}")
        set_current_mcf(__mcf)