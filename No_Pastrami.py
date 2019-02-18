sandwich_orders = ['pastrami', 'chicken', 'tuna', 'pastrami', 'mushroom', 'pastrami']

print("Deli has run out of Pastrami!!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Only the following are available: ")

for sandwich in sandwich_orders:
    print(sandwich.title())