EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Johnny Bakker",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Tommy Bakker",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Ronny Bakker",
      "locationId": 2
    }
  ]


def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee