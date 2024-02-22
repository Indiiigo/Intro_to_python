"""
Working List

    Make a list that includes four careers, such as 'programmer' and 'truck driver'.
"""
print("Part 1")
careers = ['doctor', 'scientist', 'historian', 'teacher']

print("\nUse the list.index() function to find the index of one career in your list.")
    
print(careers.index('historian'))

print("\nUse the in function to show that this career is in your list.")

print('historian' in careers)

print("\nUse the append() function to add a new career to your list.")

careers.append('politician')
print(careers)

print("\nUse the insert() function to add a new career at the beginning of the list.")

careers.insert(0, 'archeologist')
print(careers)
print("\n")

"""
Ordered Working List
"""

print("Start with the list you created in Working List.")



print("\nYou are going to print out the list in a number of different orders.")
print("Each time you print the list, use a for loop rather than printing the raw list.")
print("Print a message each time telling us what order we should see the list in.")

print("\nPrint the list in its original order.")

for career in careers:
    print(career)

print("\nPrint the list in alphabetical order.")

for career in sorted(careers):
    print(career)
        
print("\nPrint the list in reverse alphabetical order.")

for career in sorted(careers, reverse = True):
    print(career)

print("\nPermanently sort the list in alphabetical order, and then print it out.")

careers.sort()

for career in careers:
    print(career)


print("\n")
"""
List Lengths
"""

print("Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.")

languages = ['python', 'c', 'java']

print("\nPrint out a series of statements that tell us how long each list is.")

print("the new_careers list is {} items long.".format(len(careers)))
print("the languages list is {} items long.".format(len(languages))) 