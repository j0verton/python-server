import json
import sqlite3
from models import Employee, location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Sarah Ray",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Jeremy Bakker",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Alan Jeter",
        "locationId": 1
    },
    {
        "id": 4,
        "name": "Mary King",
        "locationId": 1
    },
    {
        "name": "Suzie Q",
        "locationId": 1,
        "id": 5
    }
]


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_Id
        FROM employees e
        """)
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(animal.__dict__)
    return json.dumps(employees)


def get_single_employee(id):
        with sqlite3.connect("./kennel.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.location_Id
            FROM employees e
            WHERE e.id = ?
            """, (id, ))
            data = db_cursor.fetchall()
            employee = Employee(data['id'], data['name'], data['location_id'])
        return json.dumps(employee.__dict__)


def create_employee(employee)
  max_id = EMPLOYEES[-1]["id"]
   new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id)
  employee_index = -1
   for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employees(id, new_employee)
  for index, employee in enumerate(EMPLOYEES):
       if employee["id"] == id:
        EMPLOYEES[index] = new_employee
        break
