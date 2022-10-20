# Prime Number Checker

# a function to check prime numbers
def check(numbers):
    primeNumber = []
    for number in numbers:
      if number>1:
        for i in range(2, int(number/2)+1):
          if (number % i) == 0:  # If number is divisible by any number between 2 and number / 2, it is not prime
              print(number, "is not a prime number")
              break
        else:
          print(number, "is a prime number")
          primeNumber.append(number) # add all the primenumbers numbers to the primeNumber list.
      else:
        pass
    return primeNumber # return all the prime numbers
check([2,3,4,5,6,7,8,9])
