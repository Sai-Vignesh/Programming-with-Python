# A simple program to check whether a given number is even or odd.

# get input from the user

try:   # check if the input is an integer.
    num = int(input("Enter a number: "))

    # even numbers leave a remainder zero when divided by two
    if num % 2 == 0:
        print(f"{num} is an even number")

    # if a number is not even, then it'll be odd
    else:
        print(f"{num} is an odd number")

# alerting the user to give correct input
except:
    print("Please enter a number.")
