from datetime import datetime

allowedUsers = ['Buhari', 'Burna', 'Meffy']
allowedPassword = ['Badboy2021', 'Grammyboy2021', 'CBNode2021']

username = input("What is your username?\n")

if(username in allowedUsers):
    password = input("Your Password? \n")
    userId = allowedUsers.index(username)

    if(password == allowedPassword[userId]):
        print('Welcome to Zuri Bank' + username)
        print(datetime.now())
        print('Chooose one:')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Post a Complaint')
        selectedOption = int(input('Please Select an Option'))

        if(selectedOption == 1):
            input("How much you wan withdraw?")
            print("Take your cash")
        elif(selectedOption == 2):
            balance = int(input("How much you wan deposit?"))
            print("Current balance $ %d" % balance)
        elif(selectedOption == 3):
            input("What is your complaint?")
            print("Thank you for contacting us.")
        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')
else:
    print('Name not found, please try again')





