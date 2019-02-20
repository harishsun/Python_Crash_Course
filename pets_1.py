def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")
    
pet_type = input("\nEnter the type of your pet: ")
name = input("\nEnter the name of your pet: ")

describe_pet(pet_type, name)
