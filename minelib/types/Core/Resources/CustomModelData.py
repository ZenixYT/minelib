from dataclasses import dataclass
from minelib.types.Core.Resources.Texture import Texture
import os

@dataclass
class CustomModelData:
    texture: Texture
    overridden_item: str
    custom_model_data_id: int

    def convert_to_model(self):
        # Currently it only supported generated items with 1 layer
        js = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"minecraft:item/{self.overridden_item}"
            },
            "overrides": [
                {
                    "predicate": {
                        "custom_model_data": self.custom_model_data_id
                    },
                    "model": f"minecraft:item/{os.path.splitext(os.path.basename(self.texture.path))}"
                }
            ]
        }
        return js