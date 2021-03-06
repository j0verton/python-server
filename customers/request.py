import json
import sqlite3
from models import Customer

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
    with sqlite3.connect("./kennel.db") as conn:
        conn.roe_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id
            c.name,
            c.email
        FROM customer c
        """)
        customers = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            customer = Customer(row['id'], row['name'], row['email'])
            customers.append(customer.__dict__)
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.roe_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id
            c.name,
            c.email
        FROM customer c
        WHERE c.ie = ?
        """)
        data = db_cursor.fetchone()
        customer = Customer(data['id'], data['name'], data['email'])
        return json.dumps(customer.__dict__)


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)


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
