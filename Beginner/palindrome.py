# A Palindrome Checker


# function which return reverse of a string

def isPalindrome(s):

    # remove punctuations, spaces, symbols, and make the text lower or upper
    special_char = [",", " ", "!", "@", "#", "$", "%", "^", "&", "*", "–", "_", ".",  "'", '"', ":", ";"]
    for char in special_char:
        # clean the string
        s = s.replace(char, "").lower()

    # returns true if reversed string is same as the given string
    return s == s[::-1]

ans = input("Enter the string: ")
ans = isPalindrome(ans)

if ans:
	print("Yes")
else:
	print("No")
