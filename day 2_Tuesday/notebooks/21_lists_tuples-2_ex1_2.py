print("Gymnast Scores")

print("Store the possible scores a gymnast can earn from one judge in a list.")

scores = []
for score in range(1,11):
	scores.append(score)

print("\nPrint out the sentence, \"The lowest possible score is ___, and the highest possible score is ___.\" Use the values from your list.")

print("The lowest possible score is {0}, and the highest possible score is {1}.".format(scores[0], scores[-1]))


print("\nPrint out a series of sentences, \"A judge can give a gymnast ___ points.\"")
print("\nDon't worry if your first sentence reads \"A judge can give a gymnast 1 points.")

for score in scores:
	print("A judge can give a gymnast {} points.".format(score))


print("\nHowever, you get 1000 bonus internet points if you can use a for loop, and have correct grammar.")

print("A judge can give a gymnast {} point.".format(scores[0]))
for score in scores[1:]:
	print("A judge can give a gymnast {} points.".format(score))

print("\nPop the first five elements (by position) and remove the last(by value).")
for score in range(1,5):
	scores.pop(0)

print(scores)

scores.remove(10)

print(scores)