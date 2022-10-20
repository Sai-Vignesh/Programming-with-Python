# simple contact book program
print("-----------------PHONE BOOK-----------------")
print("0. QUIT")
print("1. ADD PHONE NUMBERS TO THE PHONE BOOK.")
print("2. SEARCH PHONE NUMBER IN THE PHONE BOOK")
contacts = {} # dictionary to store name: number
while True:
    x = int(input("enter NUMBER[0/1/2]:- ")) # edit and search PHONEBOOK
    if x == 1:
        name = input("enter name: ")
        phone = input("enter phone number: ")
        contacts[name] = phone # add new elements to dictionary
    elif x == 2:
        search_name = input("enter a NAME to search for a phone number in PHONE BOOK: ")
        print(f"Phone number of {search_name} is {contacts[search_name]}") # search the dictionary
    elif x == 0:
        print("closing PHONE BOOK")
        break # exits the program
