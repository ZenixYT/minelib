from dataclasses import dataclass
import os

@dataclass
class Texture:
    path: str

    def convert_to_model(self):
        # Currently it only supported generated items with 1 layer
        js = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"minecraft:item/{os.path.splitext(os.path.basename(self.path))}"
            }
        }
        return js