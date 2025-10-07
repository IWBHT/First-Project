#make a program where the computer gives the user a random target which the user has to then add or subtract to reach
#the user is also given a random number but can choose how much ever they want to add or subtract
#the user should have 5 chances, but shouldn't be notified until they have 2 chances left
#but every time the user gets the question incorrect the given number changes
# Every questions the user gets right they get a point but every question they get wrong a point gets removed
# (note: the player isn't allowed to go into a negative score)
#DONE 10/1/25
import random

print("[Random Addition and Subtraction Practice]")
print()
guesscounter = 2
score =0
# replay system
def replay():
    global score
    print("Would you like to play again? Y or N")
    rp = input("")
    rp = rp.upper()

    if rp == "Y":
        maingame()

    if rp == "N":
        if score < 0:
            print("Score 0")
        else:
            print(f"score: {score}")
            exit()


def maingame():
    global score
    while True:
        targetnum = random.randint(1,1000)
        guesses = 0
        while True:

    #make guesses checker
            if guesses > 4:
                print("sorry your out of guesses")
                replay()


    #guess notifier
            if guesses >= 3:
                global guesscounter
                print(f"you have {guesscounter} guesses left")
                guesscounter = guesscounter - 1

            givennum = random.randint(1,1000)

            print(f"the target number is {targetnum}")
            print()
            print(f"and your given number is {givennum}")
            print()
            print("Whats your operation of choice")
            print("1) Addition")
            print("2) Subtraction")


            operation = int(input(">"))
            print()





        #opperation - addition
            if operation == 1:
                guesses = guesses+1
                add = int(input("What number would you like to add? +"))
                totalA = givennum + add
                print(f"ok {add} + {givennum} = {totalA}")
                print()
                if totalA == targetnum:
                    score = score + 1

                    print("correct!!! good job ")
                    replay()

                else:
                    print("Incorrect")
                    print()
                    score = score - 1
                    continue



        #opperation - subtraction
            if operation == 2:
                guesses = guesses+1
                sub = int(input(f"What number would you want to subtract from {givennum}? -"))
                totalS = givennum - sub
                print(f"ok {givennum} - {sub} = {totalS}")
                print()
                if totalS == targetnum:
                    score = score + 1

                    print("correct!!! good job ")
                    replay()

                else:
                    print("Incorrect")
                    print()
                    score = score - 1
                    continue



maingame()




















