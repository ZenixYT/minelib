from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf

class Server:
    def __init__(self):
        pass

    def exec(self, cmd: str):
        __mcf = get_current_mcf()
        if __mcf and isinstance(__mcf, mcfunction):
            __mcf.content.append(cmd)
            set_current_mcf(__mcf)