import typing
from BaseClasses import MultiWorld, Region, Entrance, RegionType
from .Locations import CelesteLocation, locForsakenCity_table, locOldSite_table, locCelestialResort_table, \
    locGoldenRidge_table

celesteLevels = ["Forsaken City"]


def create_regions(world: MultiWorld, player: int):
    last_level = world.last_level[player].value

    menu = Region("Menu", RegionType.Generic, "menu", player, world)

    regForsakenCity = Region("Forsaken City", RegionType.Generic, "Forsaken City", player, world)
    locForsakenCity_names = [name for name, id in locForsakenCity_table.items()]
    regForsakenCity.locations += [CelesteLocation(player, loc_name, locForsakenCity_table[loc_name], regForsakenCity) for loc_name in locForsakenCity_names]
    world.regions.append(menu)
    world.regions.append(regForsakenCity)

    menu_to_forsaken_city = Entrance(player, 'Forsaken City', menu)
    menu_to_forsaken_city.connect(regForsakenCity)
    menu.exits.append(menu_to_forsaken_city)

    endRegion = regForsakenCity

    if last_level > 1:
        regOldSite = Region("Old Site", RegionType.Generic, "Old Site", player, world)
        locOldSite_names = [name for name, id in locOldSite_table.items()]
        regOldSite.locations += [
            CelesteLocation(player, loc_name, locOldSite_table[loc_name], regOldSite) for loc_name in
            locOldSite_names]
        world.regions.append(regOldSite)

        forsaken_city_to_old_site = Entrance(player, 'Old Site', endRegion)
        forsaken_city_to_old_site.connect(regOldSite)
        endRegion.exits.append(forsaken_city_to_old_site)

        endRegion = regOldSite

    if last_level > 2:
        regCelestialResort = Region("Celestial Resort", RegionType.Generic, "Celestial Resort", player, world)
        locCelestialResort_names = [name for name, id in locCelestialResort_table.items()]
        regCelestialResort.locations += [
            CelesteLocation(player, loc_name, locCelestialResort_table[loc_name], regOldSite) for loc_name in
            locCelestialResort_names]
        world.regions.append(regCelestialResort)

        old_site_to_celestial_resort = Entrance(player, 'Celestial Resort', endRegion)
        old_site_to_celestial_resort.connect(regCelestialResort)
        endRegion.exits.append(old_site_to_celestial_resort)

        endRegion = regCelestialResort

    if last_level > 3:
        regGoldenRidge = Region("Golden Ridge", RegionType.Generic, "Golden Ridge", player, world)
        locGoldenRidge_names = [name for name, id in locGoldenRidge_table.items()]
        regGoldenRidge.locations += [
            CelesteLocation(player, loc_name, locGoldenRidge_table[loc_name], regGoldenRidge) for loc_name in
            locGoldenRidge_names]
        world.regions.append(regGoldenRidge)

        celestial_resort_to_golden_ridge = Entrance(player, 'Golden Ridge', endRegion)
        celestial_resort_to_golden_ridge.connect(regGoldenRidge)
        endRegion.exits.append(celestial_resort_to_golden_ridge)

        endRegion = regGoldenRidge

#def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
#    sourceRegion = world.get_region(source, player)
#    targetRegion = world.get_region(target, player)

#    connection = Entrance(player, '', sourceRegion)
#    if rule:
#        connection.access_rule = rule

#    sourceRegion.exits.append(connection)
#    connection.connect(targetRegion)

#def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],
#                  location_cache: List[Location], name: str) -> Region:
#    region = Region(name, RegionType.Generic, name, player)
#    region.world = world

#    if name in locations_per_region:
#        for location_data in locations_per_region[name]:
#            location = create_location(player, location_data, region, location_cache)
#            region.locations.append(location)

#    return region