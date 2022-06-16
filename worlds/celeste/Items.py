from BaseClasses import Item

class CelesteItem(Item):
    game: str = "Celeste"

generic_item_table = {
    "Strawberry": 77000
}

cassette_item_table = {
    "B-Side Cassette (Forsaken City)": 77001
}

#cannon_item_table = {
#    "Cannon Unlock BoB": 3626200,
#    "Cannon Unlock WF": 3626201,
#    "Cannon Unlock JRB": 3626202,
#}

item_table = {**generic_item_table, **cassette_item_table}