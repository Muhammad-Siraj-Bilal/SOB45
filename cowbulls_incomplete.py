import random

def compare_numbers(number, user_guess):
    ## your code here
    cowbull = [0,0] # [cow,bull]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        elif user_guess[i] in number:
            cowbull[0] += 1
        else:
            continue
    return cowbull

playing = True #gotta play the game
num = str(random.randint(1000,9999))
num_li = list(num)
while (num_li[0] == num_li[1] or num_li[0] == num_li[2] or num_li[0] == num_li[3] or num_li[1] == num_li[2] or num_li[1] == num_li[3] or num_li[2] == num_li[3]):
    num = str(random.randint(1000,9999))
    num_li = list(num)
number = str(num) #random 4 digit number with every digit being different
guesses = 0
print(number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") # raw_input in version 2.
    while len(user_guess) != 4:
        user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + " guesses! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
