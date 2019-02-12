favourite_places = {
    'anju': ['london', 'new york'],
    'vig': ['chicago', 'brentwood'],
    'sarad': ['california', 'bengaluru']
}

#print(favourite_places)

for name, places in favourite_places.items():
    print("\n\tFavourite places of " + name.title() + " are: ")
    for place in places:
        print("\t" + place.title())