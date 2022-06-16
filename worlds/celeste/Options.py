import typing
from Options import Option, DefaultOnToggle, Range, Toggle, DeathLink


class DeathLinkAmnesty(Range):
    """Amount of Deaths to take before sending a DeathLink signal, for balancing difficulty"""
    range_start = 0
    range_end = 30
    default = 15

class LevelSelection(Range):
    """The number of levels to beat to finish the game"""
    range_start = 1
    range_end = 7
    default = 3

celeste_options: typing.Dict[str,type(Option)] = {
    "death_link": DeathLink,
    "DeathLinkAmnesty": DeathLinkAmnesty,
    "last_level": LevelSelection
}
