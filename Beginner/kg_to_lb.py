# A simple program to convert weight from Kilograms to Pounds

# get input from the user
weight = float(input("What is your weight? "))
# ask the user whether the program want to display weight in kgs or lbs 
unit = input("Kgs or Lbs? ").lower()
pound = 2.20462 # default lbs to kg conversion rate
converted_weight = float(weight * pound) # kg to lbs
formatted_float = "{:.2f}".format(converted_weight)


# conversion conditions
# if already given in kgs, do nothing.
if unit == "kgs" or unit == "kg" or unit == "k":
    print(f"Your weight is {weight} kgs")

# convert kgs to lbs
elif unit == "lbs" or unit == "lb" or unit == "l":
    print(f"Your weight is {formatted_float} Lbs.")

# alert the user for wrong input.
else:
    print("That is not a valid input. Please try again.")
