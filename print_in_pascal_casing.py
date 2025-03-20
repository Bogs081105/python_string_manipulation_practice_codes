#ask the user to input their name in improper casing
#store it inside a variable
full_name = input("Enter your full name in improper casing: ")

#modify the variable into pascal casing, remove the spaces and organize the casing
#print the result
print(full_name.title().replace(" ", ""))