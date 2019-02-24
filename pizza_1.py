def make_pizza(*toppings):
    print("\nMaking pizza with the follwing toppings: ")
    for topping in toppings:
        print(" - " + topping)


make_pizza('pepporoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

