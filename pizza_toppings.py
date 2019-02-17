prompt = "\nEnter your choice of Pizza topings: "
prompt += "\nEnter quit to stop: "

message = ""
while message != 'quit':
    message = input(prompt)
    print("Your topping " + message.title() + " is added to the pizza!")