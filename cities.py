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
        'country': 'usa',
        'population': 8.623,
        'fact': 'The first American chess tournament was held in New York'
    }

}

for city, city_info in cities.items():
    print("\n\t" + city.title())
    print("\t******************")
    country_info = city_info['country']
    population_info = city_info['population'] 
    fact_info = city_info['fact']

    print("\tCountry: " + country_info.title())
    print("\tPopulation: " + str(population_info) + " million")
    print("\tFact: " + fact_info)