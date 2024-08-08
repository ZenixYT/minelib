from minelib.types.Core.EntitySpecifier import EntitySpecifier, TargetSelector
from minelib.minecraft.mcfunction import mcfunction, get_current_mcf, set_current_mcf
from minelib.types.Core.TextComponent import TextComponent
from minelib.types.Items.ItemStack import ItemStack, ItemMeta
from minelib.types.Core.Location import Location
from minelib.types.Core.Execute import Execute

class Player:
    def __init__(self, spec: EntitySpecifier):
        self.spec = spec

    def chat(self, text: str):
        __mcf = get_current_mcf()
        __mcf.content.append(f"execute as {self.spec.to_string()} run say {text}")
        set_current_mcf(__mcf)

    def print(self, text: TextComponent | str):
        __mcf = get_current_mcf()
        if isinstance(text, TextComponent):
            __mcf.content.append(f"tellraw {self.spec.to_string()} {text.dump()}")
        elif isinstance(text, str):
            __mcf.content.append(f'tellraw {self.spec.to_string()} "{text}"')
        set_current_mcf(__mcf)

    def give_item(self, item: ItemStack):
        __mcf = get_current_mcf()
        __mcf.content.append(f"give {self.spec.to_string()} {item.get_mc_str()} {item.count}")
        set_current_mcf(__mcf)

    def teleport(self, loc: Location | EntitySpecifier):
        if isinstance(loc, Location):
            Execute().as_(self.spec).run_command(f"tp @s {loc.to_string()}")
        elif isinstance(loc, EntitySpecifier):
            Execute().as_(self.spec).run_command(f"tp @s {loc.to_string()}")

    def mount(self, entity: EntitySpecifier):
        Execute().as_(self.spec).run_command(f"ride @s mount {entity.to_string()}")
    
    def unmount(self):
        Execute().as_(self.spec).run_command(f"ride @s unmount")

    def add_tags(self, tags: str | list[str]):
        if isinstance(tags, str):
            Execute().as_(self.spec).run_command(f"tag @s add {tags}")
        else:
            for tag in tags:
                Execute().as_(self.spec).run_command(f"tag @s add {tag}")

    def remove_tags(self, tags: str | list[str]):
        if isinstance(tags, str):
            Execute().as_(self.spec).run_command(f"tag @s remove {tags}")
        else:
            for tag in tags:
                Execute().as_(self.spec).run_command(f"tag @s remove {tag}")

    def apply_effects(self, effects: str | list[str], time: int, should_show_particles: bool = True):
        if isinstance(effects, str):
            Execute().as_(self.spec).run_command(f"effect give @s {effects} {time} {should_show_particles}")
        else:
            for effect in effects:
                Execute().as_(self.spec).run_command(f"effect give @s {effect} {time} {should_show_particles}")

    def clear_effects(self, effects: str | list[str] = None):
        if effects is not None:
            if isinstance(effects, str):
                Execute().as_(self.spec).run_command(f"effect clear @s {effects}")
            else:
                for effect in effects:
                    Execute().as_(self.spec).run_command(f"effect clear @s {effect}")
        else:
            Execute().as_(self.spec).run_command(f"effect clear @s")