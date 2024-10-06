#Exercises
"""

First Neat List

    Store the values 'python', 'c', and 'java' in a list. Print a statement about each of these values, 
    using their position in the list.
    Your statement could simply be, 'A nice programming language is value.'

"""


languages = ['python', 'c', 'java']

print("A nice programming language is " + languages[0])
print("A nice programming language is " + languages[1])
print("A nice programming language is {}".format(languages[2]))


print("\n")


"""

Your First List

    Think of something you can store in a list. Make a list with three or four items, 
    and then print a message that includes at least one item from your list. 
    Your sentence could be as simple as, "One item in my list is a ____."

"""

my_list = [3, 'my CD', 'Kessler', 2.5]

print("The thing that I cannot live without is {}.".format(my_list[1]))
