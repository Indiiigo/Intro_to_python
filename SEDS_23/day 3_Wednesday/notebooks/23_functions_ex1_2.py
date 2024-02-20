def calculate_sum(number_1, number_2):
    sum_ = number_1 + number_2
    return sum_

number_lists = [[1, 1], [1, 2], [20, 10]]
for n_1, n_2 in number_lists:
    output = calculate_sum(n_1, n_2)
    print("{} + {} = {}".format(n_1, n_2, output))