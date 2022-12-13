import typing
from Options import Option, DefaultOnToggle, Range, Toggle, DeathLink


class DeathLinkAmnesty(Range):
    """Amount of deaths to take before sending a DeathLink signal, for balancing difficulty"""
    range_start = 0
    range_end = 1000
    default = 100

class LevelSelection(Range):
    """The number of levels to beat to finish the game"""
    range_start = 1
    range_end = 9
    default = 3

celeste_options: typing.Dict[str, typing.Type(Option)] = {
    "death_link": DeathLink,
    "death_link_amnesty": DeathLinkAmnesty,
    "last_level": LevelSelection
}
