def describe_person(name, favourite_color="green", favourite_game=None):
    print("Hi, this is {}.".format(name.title()))
    
    if favourite_color:
        print("My favourite color is {}.".format(favourite_color))
    else:
        print("I have no favourite color.")
    
    if favourite_game:
        print("My favourite game is {}.".format(favourite_game))
    else:
        print("I have no favourite game.")
    print("\n")

describe_person("ken")
describe_person("ADELE", favourite_color="black", favourite_game="backgammon")
describe_person("Brian", favourite_color=None, favourite_game="chess")
describe_person("Brian", favourite_game="chess")