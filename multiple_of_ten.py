number = input("Enter a number, and i will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print("The number " +  str(number) + " is a multiple of 10")

else:
    print("The number " + str(number) + " is not a multiple of 10")