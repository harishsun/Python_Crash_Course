class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age, place):
        """initialize name and age attribute"""
        self.name = name
        self.age = age
        self.place = place
        #print('*************')
        #print(age)

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting at " + self.place.title() )

    def roll_over(self):
        """Simulate rolling over response to a command"""
        print(self.name.title() + " is rolled over!")


my_dog = Dog('willie', 6, 'brentwood')
#~~~~~Accessing attributes~~~~~~~~#

print(my_dog.name.title())
print(str(my_dog.age))

#~~~~~Calling methods~~~~#
my_dog.sit()
my_dog.roll_over()
