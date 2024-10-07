# Mountain Heights

#    Wikipedia has a list of the tallest mountains in the world, with each mountain's elevation. Pick five mountains from this list.
print("Create a dictionary with the mountain names as keys, and the elevations as values.")

mountain_dict = {"Mount Everest": 8448, "K2": 8611, "Kanchenjunga":8586, "Lhotse" : 8516, "Cho Oyu" : 8201}

print("\n")
print("Print out just the mountains\' names, by looping through the keys of your dictionary.")
for key in mountain_dict.keys():
    print(key)

print("\n")
print("Print out just the mountains' elevations, by looping through the values of your dictionary.")
for val in mountain_dict.values():
    print(val)

print("\n")
print("Print out a series of statements telling how tall each mountain is: \"Everest is 8848 meters tall.\"")
for key, val in mountain_dict.items():
    print("%s is %d meters tall." %(key,val))