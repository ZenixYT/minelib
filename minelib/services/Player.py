from enum import Enum
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.PlayerSpecifier import PlayerSpecifier

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

    def give_item(self, item_id: str, destined_player: str | PlayerSpecifier, count: int = 1):
        __mcf = get_current_mcf()
        if isinstance(__mcf, mcfunction):
            __mcf.content.append(f'give {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {item_id} {count}')
            set_current_mcf(__mcf)