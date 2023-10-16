print("####### Gymnast Scores - 2")
scores = range(1, 11)

for score in scores:
    # if score != 1:
    # if score >= 2:
    if score > 1:
        print("A judge can give a gymnast {} points.".format(score))
    else:
        print("A judge can give a gymnast {} point.".format(score))
        
print("\n####### Numbers")
saved_numbers = [2, 1, 5, 12, 42, 34, 52]
new_numbers = [3, 1, 33, 52, 4]

for new_number in new_numbers:
    if new_number not in saved_numbers:
        saved_numbers.append(new_number)
        print("{} is now saved".format(new_number))
    else:
        print("{} is already saved".format(new_number))