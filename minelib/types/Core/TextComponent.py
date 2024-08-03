from enum import Enum, auto

class TextFormat(Enum):
    RESET = auto()
    ITALIC = auto()
    UNDERLINE = auto()
    STRIKETHROUGH = auto()
    BOLD = auto()
    OBFUSCATED = auto()

class TextColor(Enum):
    BLACK = "black"
    DARK_BLUE = "dark_blue"
    DARK_GREEN = "dark_green"
    DARK_AQUA = "dark_aqua"
    DARK_RED = "dark_red"
    DARK_PURPLE = "dark_purple"
    GOLD = "gold"
    GRAY = "gray"
    DARK_GRAY = "dark_gray"
    BLUE = "blue"
    GREEN = "green"
    AQUA = "aqua"
    RED = "red"
    LIGHT_PURPLE = "light_purple"
    YELLOW = "yellow"
    WHITE = "white"

class TextComponent:
    text: str
    color: TextColor = None
    format: list[TextFormat] = None

    def __init__(self, text: str, color: TextColor = None, format: TextFormat | list[TextFormat] = None):
        self.text = text
        self.color = color
        self.format = [format] if isinstance(format, TextFormat) else format if format is not None else []

    def dump(self, include_apostrophes=True):
        new_json = {"text": self.text}
        if self.color is not None:
            new_json.update({"color": TextColor.value})
        if len(self.format) > 0:
            for format in self.format:
                new_json.update({format.name.lower(): True})

        return new_json