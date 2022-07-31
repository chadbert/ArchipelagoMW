from BaseClasses import Location


class CelesteLocation(Location):
    game: str = 'Celeste'

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

locCelestialResort_table = {
    'Start 1/11': 2727138,
    'Start 2/11': 2727139,
    'Start 3/11': 2727140,
    'Start 4/11': 2727141,
    'Start 5/11': 2727142,
    'Start 6/11': 2727143,
    'Start 7/11': 2727144,
    'Start 8/11': 2727145,
    'Start 9/11': 2727146,
    'Start 10/11': 2727147,
    'Start 11/11': 2727148,
    'Huge Mess 1/7': 2727149,
    'Huge Mess 2/7': 2727150,
    'Huge Mess 3/7': 2727151,
    'Huge Mess 4/7': 2727152,
    'Huge Mess 5/7': 2727153,
    'Huge Mess 6/7': 2727154,
    'Huge Mess 7/7': 2727155,
    'Elevator Shaft 1/4': 2727156,
    'Elevator Shaft 2/4': 2727157,
    'Elevator Shaft 3/4': 2727158,
    'Elevator Shaft 4/4': 2727159,
    'Presidential Suite 1/3': 2727160,
    'Presidential Suite 2/3': 2727161,
    'Presidential Suite 3/3': 2727162
}

locGoldenRidge_table = {
    'Start 1/8': 2727163,
    'Start 2/8': 2727164,
    'Start 3/8': 2727165,
    'Start 4/8': 2727166,
    'Start 5/8': 2727167,
    'Start 6/8': 2727168,
    'Start 7/8': 2727169,
    'Start 8/8': 2727170,
    'Shrine 1/9': 2727171,
    'Shrine 2/9': 2727172,
    'Shrine 3/9': 2727173,
    'Shrine 4/9': 2727174,
    'Shrine 5/9': 2727175,
    'Shrine 6/9': 2727176,
    'Shrine 7/9': 2727177,
    'Shrine 8/9': 2727178,
    'Shrine 9/9': 2727179,
    'Old Trail 1/7': 2727180,
    'Old Trail 2/7': 2727181,
    'Old Trail 3/7': 2727182,
    'Old Trail 4/7': 2727183,
    'Old Trail 5/7': 2727184,
    'Old Trail 6/7': 2727185,
    'Old Trail 7/7': 2727186,
    'Cliff Face 1/5': 2727187,
    'Cliff Face 2/5': 2727188,
    'Cliff Face 3/5': 2727189,
    'Cliff Face 4/5': 2727190,
    'Cliff Face 5/5': 2727191
}


location_table = {**locForsakenCity_table, **locOldSite_table, **locCelestialResort_table, **locGoldenRidge_table}
