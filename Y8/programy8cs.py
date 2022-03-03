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


processUserLogin()

print()

#enter 6 lengths
print("Enter six lengths below:")

print()

one = str(input("Enter length 1: "))
two = str(input("Enter length 2: "))
print("Other lengths skipped")

print()


#sort lengths

if(one>two):
    print("Length 1 is bigger")
    length = str("Length 1 is bigger")
elif(one<two):
    print("Length 2 is bigger")
    length = str("Length 2 is bigger")
elif(one==two):
    print("Both lengths are equal")
    length=str("Both Lengths are equal")
else:
    print("Unknown error in sorting lengths")

print()


#show quiz

print("Quiz time!")
print()

q1 = str(input("How can cold water affect your swimming capability? \n a. It does not \n b. It is harder to swim as you get cramp \n c. It is easier to swim as you cool down \nType your correct answer (a, b, c, d): "))

if(q1 == "b"):
        print("Correct Answer")
        answer = str("b, correct")
else:
    print("Incorrect answer")
    answer = str("incorrect option, incorrect")
print("Other questions skipped")





#show results
print("Your Result:")
print()
def results():
    print("-----------------------------------------------------")
    print("|              Riverside Swimming Club               |")
    print("| Length 1: " + one + "                                        |")
    print("| Length 2: " + two + "                                        |")
    print("| Bigger length: " + length + "                  |")
    print("| Quiz: " + answer + "                                   |")
    print("-----------------------------------------------------")

#call functions

results()

print()
print("Thank you for using our app!")
print()
log_out = "no"
while(log_out == "no"):
    input("Press enter log out, clear data and exit")
    exit = input("Are you sure you want to exit (Y/N): ")
    if(exit=="N"):
        log_out = "no"
    elif(exit=="Y"):
        log_out = "yes"
    else:
        print("Type Y/N only")