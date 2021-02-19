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

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customerp["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer-INDEX)

def update_customers(id, new_customer):
    for index, customer in enumerate(CUSTOMERS)
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
