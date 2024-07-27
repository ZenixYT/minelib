from enum import Enum
from minelib.minecraft.mcfunction import get_current_mcf, set_current_mcf, mcfunction
from minelib.types.PlayerSpecifier import PlayerSpecifier

class Player:
    def __init__(self):
        pass

    def give_item(self, item_id: str, destined_player: str | PlayerSpecifier, count: int = 1):
        __mcf = get_current_mcf()
        if isinstance(__mcf, mcfunction):
            __mcf.content.append(f'give {destined_player.value if isinstance(destined_player, PlayerSpecifier) else destined_player} {item_id} {count}')
            set_current_mcf(__mcf)