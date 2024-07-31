from enum import Enum
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.types.EntitySpecifier import EntitySpecifier
from minelib.types.ItemStack import ItemStack, ItemMeta
from minelib.types.Location import Location
from typing import Iterable

class Player:
    def __init__(self):
        pass

    def chat(self, text: str, destined_player: EntitySpecifier):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {destined_player.to_string()} run say {text}")
        set_current_mcf(__mcf)

    def print_to_player(self, text: str, destined_player: EntitySpecifier):
        __mcf = get_current_mcf()
        if __mcf and isinstance(__mcf, mcfunction):
            __mcf.content.append(f'tellraw {destined_player.to_string()} "{text}"')
            set_current_mcf(__mcf)
        else:
            print("Error: __mcf is not defined or is not of type mcfunction.")

    def give_item(self, item: ItemStack, destined_player: EntitySpecifier):
        __mcf = get_current_mcf()
        if isinstance(__mcf, mcfunction):
            item_str = item.get_mc_str()
            __mcf.content.append(f'give {destined_player.to_string()} {item_str} {item.count}')
            set_current_mcf(__mcf)

    def teleport(self, player: EntitySpecifier, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.to_string()} run tp @s {loc.X} {loc.Y} {loc.Z}")
        set_current_mcf(__mcf)

    def teleport_relative(self, player: EntitySpecifier, loc: Location):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.to_string()} at @s run tp @s ~{loc.X if loc.X != 0 else ''} ~{loc.Y if loc.Y != 0 else ''} ~{loc.Z if loc.Z != 0 else ''}")
        set_current_mcf(__mcf)

    def teleport_to_entity_or_player(self, player: EntitySpecifier, entity: EntitySpecifier):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {player.to_string()} run tp @s {entity.to_string()}")
        set_current_mcf(__mcf)

    def ride_entity(self, player: EntitySpecifier, entity: EntitySpecifier):
        __mcf = get_current_mcf()
        __mcf.content.append(f"ride {player.to_string()} mount {entity.to_string()}")
        set_current_mcf(__mcf)

    def add_tags(self, player: EntitySpecifier, tags: str | list[str]):
        __mcf = get_current_mcf()
        if isinstance(tags, str):
            __mcf.content.append(f"tag {player.to_string()} add {tags}")
        else:
            for tag in tags:
                __mcf.content.append(f"tag {player.to_string()} add {tag}")
        set_current_mcf(__mcf)

    def remove_tags(self, player: EntitySpecifier, tags: str | list[str]):
        __mcf = get_current_mcf()
        if isinstance(tags, str):
            __mcf.content.append(f"tag {player.to_string()} remove {tags}")
        else:
            for tag in tags:
                __mcf.content.append(f"tag {player.to_string()} remove {tag}")
        set_current_mcf(__mcf)