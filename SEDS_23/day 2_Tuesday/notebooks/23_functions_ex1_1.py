def greet(first_name, last_name):
    # print("Hello {} {}".format(first_name, last_name))
    # print("I wish you a very nice day.")
    
    print("Hello {} {},\nI wish you a very nice day.\n".format(first_name, last_name))

people = [["Adriana", "Schmidt"], ["Billy", "Müller"], ["Caroline", "Schneider"]]
for first_name, last_name in people:
    greet(first_name, last_name)

# for person_data in people:
#     greet(person_data[0], person_data[1])