print("First Twenty")

print("Use the range() function to store the first twenty numbers (1-20) in a list, and print them out.")

first_twenty = range(1,21)

for number in first_twenty:
	print(number)

print("\nFive Wallets")

print("Imagine five wallets with different amounts of cash in them. Store these five values in a list")

wallets = [2000, 12, 456, 9, 10000]

print("The fattest wallet has {} in it.".format(sorted(wallets, reverse = True)[0]))
print("The skinniest wallet has {} in it.".format(sorted(wallets)[0]))
print("All together, these wallets have $ {} in them.".format(sum(wallets)))