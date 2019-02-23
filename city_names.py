def city_country(city_name, country_name):

    formatted_string = (city_name + "," + country_name)
    return formatted_string.title()


city_details = city_country('santiago', 'chile')

print(city_details)