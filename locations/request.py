LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville Kennels North",
      "address": "200 Main St",
      "animalId": 1,
      "employeeId": 1
    },
    {
      "id": 2,
      "name": "Nashville Kennels South",
      "address": "2000 Main St",
      "animalId": 2,
      "employeeId": 1
    }
  ]


def get_all_locations():
    return LOCATIONS

    # Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locations list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location