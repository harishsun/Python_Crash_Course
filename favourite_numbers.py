favourite_numbers = {
    'musk': [1, 3, 5, 7, 9],
    'jobs': [2, 4, 6, 8, 10],
    'gates': [1, 2, 3, 4, 5],
    'may': [1, 2, 3, 7, 9],
    'scarlet': [2, 5, 7, 10, 12]
}

for name, numbers in favourite_numbers.items():
    print("\n\tFavourite number of " + name.title() + " are:")
    for number in numbers:
        print("\t" + str(number))