from enum import Enum
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.types.ItemStack import ItemStack, ItemMeta
from minelib.types.Location import Location

class Player:
    def __init__(self):
        pass

    def print_to_player(self, text: str, destined_player: str | PlayerSpecifier):
        __mcf = get_current_mcf()
        if __mcf and isinstance(__mcf, mcfunction):
            __mcf.content.append(f'tellraw {destined_player.value} "{text}"')
            set_current_mcf(__mcf)
        else:
            print("Error: __mcf is not defined or is not of type mcfunction.")

    def give_item(self, item: ItemStack, destined_player: str | PlayerSpecifier):
        __mcf = get_current_mcf()
        if isinstance(__mcf, mcfunction):
            item_str = item.get_mc_str()
            __mcf.content.append(f'give {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {item_str} {item.count}')
            set_current_mcf(__mcf)

    def teleport(self, player: str | PlayerSpecifier, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.value if isinstance(player, PlayerSpecifier) else player} run tp @s {loc.X} {loc.Y} {loc.Z}")
        set_current_mcf(__mcf)

    def teleport_relative(self, player: str | PlayerSpecifier, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.value if isinstance(player, PlayerSpecifier) else player} at @s run tp @s ~{loc.X if loc.X != 0 else ''} ~{loc.Y if loc.Y != 0 else ''} ~{loc.Z if loc.Z != 0 else ''}")
        set_current_mcf(__mcf)

    def teleport_to_entity_or_player(self, player: str | PlayerSpecifier, entity: str | PlayerSpecifier):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.value if isinstance(player, PlayerSpecifier) else player} run tp @s {entity.value if isinstance(entity, PlayerSpecifier) else entity}")
        set_current_mcf(__mcf)

    def ride_entity(self, player: str | PlayerSpecifier, entity: str | PlayerSpecifier):
        __mcf = get_current_mcf()
        __mcf.content.append(f"ride {player.value if isinstance(player, PlayerSpecifier) else player} mount {entity.value if isinstance(entity, PlayerSpecifier) else entity}")
        set_current_mcf(__mcf)