def make_sandwiches(*fillings):
    print("\n----Making Sandwich with the following fillings---- ")
    for filling in fillings:
        print(" - " + filling.title())




make_sandwiches('egg')
make_sandwiches('tomato', 'cucumber')
make_sandwiches('pickles', 'jalapenos', 'olives')
