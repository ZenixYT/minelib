from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf

class World:
    def __init__(self):
        pass

    def set_time_of_day(self, time: int):
        __mcf = get_current_mcf()
        __mcf.content.append(f"time set {time}t")
        set_current_mcf(__mcf)