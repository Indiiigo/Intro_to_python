pets = {'Tom': 'cat', 'Spike' : 'dog', 'Jerry' : 'mouse', 'Remi' : 'rat'}

pets['Tom'] = 'Persian cat'
print(pets)

pets['Black Beauty'] = 'horse'
print(pets)

del pets['Black Beauty']
print(pets)

print("Bonus")

for key, val in pets.items():
	print( "%s : %s" %(key,val))
