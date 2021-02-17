from animals.request import ANIMALS


CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "email@aol.com"
    },
    {
        "id": 2,
        "name": "Sally Anne",
        "address": "7002 Chestnut Ct",
        "email": "email@aol.com"
    },
    {
        "id": 3,
        "name": "Jeff Stevens",
        "address": "7002 Chestnut Ct",
        "email": "email@aol.com"
    },
    {
        "email": "jeff@jeff.com",
        "name": "Jeff Jeffity",
        "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_animal = ANIMALS

    return requested_customer
