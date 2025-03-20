#ask the user to input a number from 0-1000
#store it inside a variable
six_digits = input("Input a number from 0-1000: ")

#add zeros at the beginning until it becomes 6 digits
#print the numbers
if six_digits.isdigit() and len(six_digits) < 6:
    print(f"The number in six digits is {six_digits.zfill(6)}")
elif six_digits.isdigit() and len(six_digits) >= 6:
    print("Please enter a number from 0-1000")
