#ask the user to input a complete statement
#store inside a variable
statement = input("Please enter a complete statement: ")

#add another variable to store the modified variable
#modify the variable to count the words
word_count = len(statement.split())

#print the result
print(f"The amount of words inside the statements are: {word_count} ")