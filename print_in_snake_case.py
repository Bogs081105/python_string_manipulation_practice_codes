#ask the user to input their name in improper casing
#store inside the variable
full_name = input("Please enter your full name in improper casing: ")

#modify the variables to lowercase
#modify to replace blank spaces to _
#print the result
print(full_name.lower().replace(" ","_"))