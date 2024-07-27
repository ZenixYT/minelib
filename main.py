from minelib.Pack import Pack
from minelib.types.PlayerSpecifier import PlayerSpecifier
from minelib.logic import _mcif, _mcfor

pack = Pack("Example", "hi", 26)

@pack.function
def hi():
    pack.services.ServerService.print_to_player("Hello, world!", PlayerSpecifier.SELF)

@pack.load
def on_load():
    pack.run_function("hi", PlayerSpecifier.ALL)

pack.dump()