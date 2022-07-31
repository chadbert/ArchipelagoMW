import typing
import os, json
from .Items import item_table, CelesteItem
from .Locations import location_table
from .Options import celeste_options
from .Regions import create_regions
from BaseClasses import Region, RegionType, Entrance, Item, MultiWorld, Tutorial
from ..AutoWorld import World, WebWorld

client_version = 1


class CelesteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Celeste for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Chadbert"]
    )]


class CelesteWorld(World):
    """
     TBD
    """

    game: str = "Celeste"
    topology_present = False
    web = CelesteWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 1
    forced_auto_forfeit = False

    area_connections: typing.Dict[int, int]
    area_cost_map: typing.Dict[int,int]

    music_map: typing.Dict[int,int]

    options = celeste_options;

    def create_regions(self):
        create_regions(self.world, self.player)

    def set_rules(self):
        self.area_connections = {}
        self.area_cost_map = {}
        #set_rules(self.world, self.player, self.area_connections, self.area_cost_map)

    def create_item(self, name: str) -> Item:
        return CelesteItem(name, False, item_table[name], self.player)

    def generate_basic(self):
        last_level = self.world.last_level[self.player].value
        self.world.itempool += [self.create_item("Strawberry") for i in range(0,19)]
        #self.world.itempool.append(self.create_item("B-Side Cassette (Forsaken City)"))

        if last_level > 1:
            self.world.itempool +=[self.create_item("Strawberry") for i in range(0, 19)]

        if last_level > 2:
            self.world.itempool +=[self.create_item("Strawberry") for i in range(0,25)]

        if last_level > 3:
            self.world.itempool +=[self.create_item("Strawberry") for i in range(0,29)]

        if last_level > 4:
            self.world.itempool +=[self.create_item("Strawberry") for i in range(0,31)]

        if last_level > 6:
            self.world.itempool +=[self.create_item("Strawberry") for i in range(0,46)]

    def fill_slot_data(self):
        return {
            #"DoorCost": self.world.DoorCost[self.player].value,
            #"AreaCostRando": self.area_cost_map,
            "death_link": self.world.death_link[self.player].value,
            "death_link_amnesty": self.world.death_link_amnesty[self.player].value,
            "last_level": self.world.last_level[self.player].value
        }

    def generate_output(self, output_directory: str):
        if self.world.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.world.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }

        filename = f"AP_{self.world.seed_name}_P{self.player}_{self.world.get_file_safe_player_name(self.player)}.apv6"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)
