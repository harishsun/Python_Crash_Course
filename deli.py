sandwich_orders = ['cheese', 'chicken', 'fish', 'vegetable', 'mushroom', 'egg']

finished_sandwiches = []

while sandwich_orders:
    prep_sandwich = sandwich_orders.pop()

    print("Preparing Sandwich: " + prep_sandwich.title() + " Sandwich")
    finished_sandwiches.append(prep_sandwich)

print("\nThe following Sandwiches are ready: ")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " Sandwich")
