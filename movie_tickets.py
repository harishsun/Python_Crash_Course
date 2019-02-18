prompt = "\nWelcome to Vue cinema "
prompt += "\nPlease enter your age "
prompt += "\nEnter quit to cancel: "


while True:
    age = input(prompt)

    if age == 'quit':
        break

    elif int(age) < 3:
        print("Your age is " + age + ". So the ticket is free!")
        break

    elif int(age) >= 3 and int(age) <= 12:
        print("Your age is " + age + ". So the ticket cost's £10.")
        break

    else:
        print("Yout are age is " + age + ". So the ticket cost's £15")
        break