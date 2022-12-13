from BaseClasses import Item

class CelesteItem(Item):
    game: str = "Celeste"

generic_item_table = {
    "Strawberry": 77000,
    "Golden Strawberry": 77001,
    "Winged Golden Strawberry": 77002,
    "Moon Strawberry": 77003,

    "Key (Celestial Resort)": 77044,
    "Key (Mirror Temple)": 77045,
    "Key (Summit)": 77046,
    "Key (Core)": 77047,
    "Key (Farewell)": 77048,
    "Key": 77049
}

cassette_item_table = {
    "B-Side Cassette (Forsaken City)": 77004,
    "B-Side Cassette (Old Site)": 77005,
    "B-Side Cassette (Celestial Resort)": 77006,
    "B-Side Cassette (Golden Ridge)": 77007,
    "B-Side Cassette (Mirror Temple)": 77008,
    "B-Side Cassette (Reflection)": 77009,
    "B-Side Cassette (Summit)": 77010,
    "B-Side Cassette (Core)": 77011,

    "C-Side Cassette (Forsaken City)": 77012,
    "C-Side Cassette (Old Site)": 77013,
    "C-Side Cassette (Celestial Resort)": 77014,
    "C-Side Cassette (Golden Ridge)": 77015,
    "C-Side Cassette (Mirror Temple)": 77016,
    "C-Side Cassette (Reflection)": 77017,
    "C-Side Cassette (Summit)": 77018,
    "C-Side Cassette (Core)": 77019
}

heart_item_table = {
    "Blue Heart (Forsaken City)": 77020,
    "Blue Heart (Old Site)": 77021,
    "Blue Heart (Celestial Resort)": 77022,
    "Blue Heart (Golden Ridge)": 77023,
    "Blue Heart (Mirror Temple)": 77024,
    "Blue Heart (Reflection)": 77025,
    "Blue Heart (Summit)": 77026,
    "Blue Heart (Core)": 77027,

    "Red Heart (Forsaken City)": 77028,
    "Red Heart (Old Site)": 77029,
    "Red Heart (Celestial Resort)": 77030,
    "Red Heart (Golden Ridge)": 77031,
    "Red Heart (Mirror Temple)": 77032,
    "Red Heart (Reflection)": 77033,
    "Red Heart (Summit)": 77034,
    "Red Heart (Core)": 77035,

    "Golden Heart (Forsaken City)": 77036,
    "Golden Heart (Old Site)": 77037,
    "Golden Heart (Celestial Resort)": 77038,
    "Golden Heart (Golden Ridge)": 77039,
    "Golden Heart (Mirror Temple)": 77040,
    "Golden Heart (Reflection)": 77041,
    "Golden Heart (Summit)": 77042,
    "Golden Heart (Core)": 77043
}

item_table = {
    **generic_item_table,
    **cassette_item_table,
    **heart_item_table
}