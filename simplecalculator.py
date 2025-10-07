# make calculator that does addition, subtraction, division, multiplaction,
# exponents, and square roots
#make it so that the user restarts after every eqaution is solved
# make the calculator look nice and neat
#keep track of all the calculations the user has made
#allow the user to go back to the operartions menu incase they make a mistake
#(You can not divide by zero)
#Square root formula is exponent 1/2


History = ""

print("[Calculator]")
def main_menu():

    print("What would you like to do")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exponents")
    print("6) Square roots")
    print("7) Calculator History")
    print("8) Exit")

    choice = int(input("> "))

    if choice == 1:
        addition()

    if choice == 2:
        Subtraction()

    if choice == 3:
        Multiply()

    if choice == 4:
        Divide()

    if choice == 5:
        Exponent()

    if choice == 6:
        squareroot()

    if choice == 7:
        print(History)

    if choice == 8:
        print("Ok Bye")
        exit()

#addition
def addition():
        global History
        print("what would you like to add")
        print("if you would like to go back press enter")
        num1 = float(input(">"))
        print("+")
        num2 = float(input(">"))
        if num1 != str:
            main_menu()
        total = num1 + num2
        print(f"{num1} + {num2} = {total}")
        History = History + f"{num1} + {num2} = {total}\n"
        returnmen = input("press any button to return to main menu ")
        if returnmen == 1 or returnmen != "a" or returnmen == "a":
            main_menu()







#Subtraction
def Subtraction():
        global History
        print("what would you like to subtract")
        num1 = float(input(">"))
        print("-")
        num2 = float(input(">"))
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
        History = History + f"{num1} - {num2} = {total}\n"
        returnmen = input("press any button to return to main menu ")
        if returnmen == 1 or returnmen != "a" or returnmen == "a":
            main_menu()



#Multiply
def Multiply():
        global History
        print("what would you like to Multiply")
        num1 = float(input(">"))
        print("x")
        num2 = float(input(">"))
        total = num1 * num2
        print(f"{num1} x {num2} = {total}")
        History = History + f"{num1} x {num2} = {total}\n"
        returnmen = input("press any button to return to main menu ")
        if returnmen == 1 or returnmen != "a" or returnmen == "a":
            main_menu()




#Division
def Divide():
    while True:
        global History
        print("what would you like to Divide")
        num1 = float(input(">"))
        print("/")
        num2 = float(input(">"))
        if num2 == 0:
            print("Sorry you cannot divide by zero")
        else:
            total = num1 / num2
            print(f"{num1} / {num2} = {total}")
            History = History + f"{num1} / {num2} = {total}\n"
            returnmen = input("press any button to return to main menu ")
            if returnmen == 1 or returnmen != "a" or returnmen == "a":
                main_menu()


#Exponent
def Exponent():
        global History
        print("what would exponent would you like to add to your base")
        num1 = float(input("Whats your base? >"))
        print("^")
        num2 = float(input("Whats your exponent? >"))
        total = num1 ** num2
        print(f"{num1} ^ {num2} = {total}")
        History = History + f"{num1} ^ {num2} = {total}\n"
        returnmen = input("press any button to return to main menu ")
        if returnmen == 1 or returnmen != "a" or returnmen == "a":
            main_menu()


#Squareroot
def squareroot():
    while True:
        global History
        print("what would you like to know the square root of ")
        num1 = int(input(">"))
        if num1 == 0:
            print("Sorry you cannot get the square root of 0")
        else:
            total = num1 ** 0.5
            print(f"the square root of {num1} is {total}")
            print()
            if num1 % total ==0:
                print("That's a perfect square!")
                print()


        History = History + f"the square root of {num1} is {total}\n"
        returnmen = input("press any button to return to main menu ")
        if returnmen == 1 or returnmen != "a" or returnmen == "a":
            main_menu()


main_menu()


