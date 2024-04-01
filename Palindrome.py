#Palindrome

value = input("Is it a palindrome?: ")
value=value.lower()
list(value)

opposite = value[::-1]

if value == opposite:
    print("Yes",value, "is a palindrome.")
else:
    print("No",value, "is not a palindrome.")
