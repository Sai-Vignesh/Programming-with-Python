# Guess the number

ans = 9 # number to guess
print("Can you guess the number?")

answered = False
for i in range(3):
    response = input("Guess the number: ") # ask the user to guess
    if int(response) == ans: # check whether the guess is correct
        print("You win!") # cheers
        answered = True
        break # break the loop
    else:  # try again
        if i < 2:
            print("Try again...")
if not answered:
    print("You loose.")
print("Thanks for playing.") # thanks
