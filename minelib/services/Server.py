# Server.py
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf

class Server:
    def __init__(self):
        pass

    def print_to_player(self, text: str, destined_player: str | PlayerSpecifier):
        __mcf = get_current_mcf()
        if __mcf and isinstance(__mcf, mcfunction):
            __mcf.content.append(f'tellraw {destined_player.value} "{text}"')
            set_current_mcf(__mcf)
        else:
            print("Error: __mcf is not defined or is not of type mcfunction.")

    def exec(self, cmd: str):
        __mcf = get_current_mcf()
        if __mcf and isinstance(__mcf, mcfunction):
            __mcf.content.append(cmd)
            set_current_mcf(__mcf)