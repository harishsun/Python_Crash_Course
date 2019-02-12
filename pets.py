

boris = {
    'animal': 'tiger',
    'owner_name': 'tyson'
}

lucifier = {
    'animal': 'goat',
    'owner_name': 'constantine'
}

ghost = {
    'animal': 'wolf',
    'owner_name': 'snow'
}

drogon = {
    'animal': 'dragon',
    'owner_name': 'daenerys'
}

sully = {
    'animal': 'dog',
    'owner_name': 'bush'
}

jumbo = {
    'animal': 'elephant',
    'owner_name': 'appu'
}

bolt = {
    'animal': 'dog',
    'owner_name': 'travolta'
}



pets = [boris, lucifier, ghost, drogon, sully, jumbo, bolt]

for pet_details in pets:
    pet_type = pet_details['animal']
    pet_owner = pet_details['owner_name']

    print("\t Pet: " + pet_type.title())
    print("\t Owner: " + pet_owner.title() + "\n")


