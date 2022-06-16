from BaseClasses import Location


class CelesteLocation(Location):
    game: str = 'Celeste'


# Forsaken City
locForsakenCity_table = {
    'Forsaken City Start 1/6': 2727100,
    'Forsaken City Start 2/6': 2727101,
    'Forsaken City Start 3/6': 2727102,
    'Forsaken City Start 4/6': 2727103,
    'Forsaken City Start 5/6': 2727104,
    'Forsaken City Start 6/6': 2727105,
    'Forsaken City Crossing 1/9': 2727106,
    'Forsaken City Crossing 2/9': 2727107,
    'Forsaken City Crossing 3/9': 2727108,
    'Forsaken City Crossing 4/9': 2727109,
    'Forsaken City Crossing 5/9': 2727110,
    'Forsaken City Crossing 6/9': 2727111,
    'Forsaken City Crossing 7/9': 2727112,
    'Forsaken City Crossing 8/9': 2727113,
    'Forsaken City Crossing 9/9': 2727114,
    'Forsaken City Chasm 1/5': 2727115,
    'Forsaken City Chasm 2/5': 2727116,
    'Forsaken City Chasm 3/5': 2727117,
    'Forsaken City Chasm 4/5': 2727118,
    'Forsaken City Chasm 5/5': 2727119
}

locOldSite_table = {
    'Old Site Start 1/9': 2727120,
    'Old Site Start 2/9': 2727121,
    'Old Site Start 3/9': 2727122,
    'Old Site Start 4/9': 2727123,
    'Old Site Start 5/9': 2727124,
    'Old Site Start 6/9': 2727125,
    'Old Site Start 7/9': 2727126,
    'Old Site Start 8/9': 2727127,
    'Old Site Start 9/9': 2727128,
    'Old Site Intervention 1/8': 2727129,
    'Old Site Intervention 2/8': 2727130,
    'Old Site Intervention 3/8': 2727131,
    'Old Site Intervention 4/8': 2727132,
    'Old Site Intervention 5/8': 2727133,
    'Old Site Intervention 6/8': 2727134,
    'Old Site Intervention 7/8': 2727135,
    'Old Site Intervention 8/8': 2727136,
    'Old Site Awake': 2727137
}

# Correspond to 77000 + level index * 100 + room index
location_table = {**locForsakenCity_table, **locOldSite_table}
