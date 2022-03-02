#login
def processUserLogin():
    correct = False

    while (correct == False):
        print("      Riverside Swimming Club")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if (username == "Applicant1" and password == "Sw1mm1ng@"):
            correct = True
        else:
            correct = False
            print("Please enter correct username and password.")


#enter 6 lengths

one = int()
two = int()

def enterSixLengths():
    one = int(input("Enter length 1: "))
    two = int(input("Enter length 2: "))
    print("Other lengths skipped")

#sort lengths

length = str()

def sortLengths():
    if(one>two):
        print("Length 1 is bigger")
        length = str("L1 big")
    elif(one<two):
        print("Length 2 is bigger")
        length = str("L2 big")
    else:
        print("Unknown error in sorting lengths")

#show quiz



#show results



#call functions
processUserLogin()
enterSixLengths()
enterSixLengths()

input("Press enter to exit")