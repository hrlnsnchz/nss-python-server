CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "100 Infinity Way",
      "animalId": 3
    },
    {
      "id": 2,
      "name": "Sarah Mall",
      "address": "101 Infinity Way",
      "animalId": 1,
      "email": "blah@mail.com"
    },
    {
      "id": 3,
      "name": "Shonda Mousey",
      "address": "1000 Infinity Way",
      "animalId": 2
    },
    {
      "email": "doodles11@poodle.com",
      "name": "doodles poodle",
      "id": 4
    }
  ]

  
def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customerS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer