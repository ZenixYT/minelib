class mcfunction:
    def __init__(self, name: str, pack):
        self.name = name
        self.content: list[str] = []
        self.function_name: str = f"{pack.namespace}:{name}"

__CURRENT_MCF: mcfunction | None = None

def get_current_mcf():
    return __TEMP_CURRENT_MCF

def set_current_mcf(mcf: mcfunction):
    global __TEMP_CURRENT_MCF
    __TEMP_CURRENT_MCF = mcf