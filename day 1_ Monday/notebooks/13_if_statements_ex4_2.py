# Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
aliens = ["red", "green", "pink", "blue", "red", "blue", "green", "red", "red", "blue"]
print("number of aliens:", len(aliens))

# Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list
current_score = 0
for alien_color in aliens:
    if alien_color == "red":
        current_score = current_score + 5
    elif alien_color == "green":
        current_score = current_score + 10
    elif alien_color == "blue":
        current_score = current_score + 20
    else:
        print("I don't know points of color '{}'".format(alien_color))
print("total points: {}".format(current_score))