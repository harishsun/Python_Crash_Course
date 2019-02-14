cities = {
    'london': {
        'country': 'united kingdom',
        'population': 8.136,
        'fact': 'Big Ben was actually called Clock Tower.'
    },

    'chennai': {
        'country': 'india',
        'population': 7.8,
        'fact': 'It has the second longest beach in the world.'
    },

    'new york': {
        'country': 'united states of america',
        'population': 8.623,
        'fact': 'The first American chess tournament was held in New York'
    }

}

for city, city_info in cities.items():
    print("\n\t" + city.title())
    print("\t******************")

    for more_city, more_city_info in city_info.items():
        print("\t" + (str(more_city).title()) + ":" + str(more_city_info).title())


