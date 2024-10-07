#Exercises
"""

First Neat List - Loop

    Repeat First Neat List, but this time use a loop to print out your statements. 
    Make sure you are writing the same sentence for all values in your list. 
    Loops are not effective when you are trying to generate different output for each value in your list.

"""
languages = ['python', 'c', 'java']


for language in languages:
	print("A nice programming language is " + language)


print("\n")



"""

Your First List - Loop

    Repeat Your First List, but this time use a loop to print out your message for each item in your list.
    Again, if you came up with different messages for each value in your list, decide on one message to
    repeat for each value in your list.

"""

my_list = [3, 'my CD', 'Kessler', 2.5]

for thing in my_list:
	print("The thing that I cannot live without is {}.".format(thing))

