#ask the user to input the name with spaces at the beginning
#create a variable to modify the input
full_name = input("Enter your full name with spaces at the beginning: ")

#print the input without spaces
no_spaces = full_name.lstrip()
print(f"Name with no spaces: {no_spaces}")