# Start with users that needs to be verified
# And empty lists to hold the confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#print("+++++++++++++")
#print(unconfirmed_users)

for current_user in unconfirmed_users:
    #print(current_user)
    #current_user = x.pop()
   

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)
   

print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

    

