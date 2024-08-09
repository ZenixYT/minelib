from minelib.types.Core.Resources.Texture import Texture
from minelib.types.Core.Resources.CustomModelData import CustomModelData

class ResourcePack:
    def __init__(self):
        self.textures: list[Texture] = []
        self.model_data: list[CustomModelData] = []

    def add_new_model_data(self, overriden_item: str, texture: Texture, custom_model_data_id: int):
        mdl = CustomModelData(texture, overriden_item, custom_model_data_id)
        self.model_data.append(mdl)

    def add_new_texture(self, path: str):
        tex = Texture(path)
        self.textures.append(tex)

    def dump(self):
        pass #TODO: Implement resource packs