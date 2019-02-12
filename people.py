

person_0 = {
    'first': 'steve',
    'last': 'jobs',
    'age': 77,
    'location': 'heaven'
}

person_1 = {
    'first': 'bill',
    'last': 'gates',
    'age': 72,
    'location': 'seatle'
}

person_2 = {
    'first': 'elon',
    'last': 'musk',
    'age': 52,
    'location': 'california'
}


people = [person_0, person_1, person_2]

for person in people:
    fullname = person['first'] + " " + person['last']
    age = person['age']
    location = person['location']

    print("\tFullname: " + fullname.title())
    print("\tAge: " + str(age))
    print("\tLocation: " + location.title() + "\n")
    
    
