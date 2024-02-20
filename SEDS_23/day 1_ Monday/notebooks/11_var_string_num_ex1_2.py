print("####### Part 1:")
# Store the quote in a variable.
quote = "One of my most productive days was throwing away 1000 lines of code"
# Store the full name of the person in another variable.
person = "Ken Thompson"

# Print a sentence in such format "X once said, 'quote comes here'." 
sentence = "{} once said, '{}'.".format(person, quote)
print(sentence)

print("####### Part 2:")
# Store a first name and a last name, in lowercase, in 2 different variables.
first_name = "name"
last_name = "surname"
# Using that variables store the full name in another variable (concatenation)
full_name = first_name + " " + last_name
# full_name = "{} {}".format(first_name, last_name)

# Print the full name in lowercase, Titlecase, and UPPERCASE.
print(full_name)
print(full_name.lower())
print(full_name.title())
print(full_name.upper())