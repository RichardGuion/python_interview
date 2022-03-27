import pytest

'''
    find top 2 numbers in an unsorted list
'''

# method 1 using sort
def find_max(num_list, top_numbers):
    num_list.sort(reverse=True)
    return num_list[0:top_numbers]


@pytest.mark.parametrize("num_list, top_numbers, expected_output", [
    ([2, 7, 11, 15], 2, [15, 11]),
    ([11, 7, 15, 2, 0, 13], 2, [15, 13]),
    ([-33, -1, -44, -2, -55, -77], 2, [-1, -2])
])
def test_find_max(num_list, top_numbers, expected_output):
    assert find_max(num_list, top_numbers) == expected_output


# method 2 without using sort
# create a new sorted list in reverse
# performance is slow because we loop thru the list multiple times
def find_max2(num_list, top_numbers):
    new_list = []
    while num_list:
        maximum = num_list[0]  # arbitrary number in list
        for x in num_list:
            if x > maximum:
                maximum = x
        new_list.append(maximum)
        num_list.remove(maximum)
    return new_list[0:top_numbers]


@pytest.mark.parametrize("num_list, top_numbers, expected_output", [
    ([2, 7, 11, 15], 2, [15, 11]),
    ([11, 7, 15, 2, 0, 13], 2, [15, 13]),
    ([-33, -1, -44, -2, -55, -77], 2, [-1, -2])
])
def test_find_max2(num_list, top_numbers, expected_output):
    assert find_max2(num_list, top_numbers) == expected_output


# without sorting, just finding two numbers
def find_top_max_numbers(num_list):
    max = num_list[0]
    second_max = 0
    for n in num_list:
        if n > max:
            second_max = max
            max = n
        elif n > second_max:
            second_max = n
    return (max, second_max)


@pytest.mark.parametrize("num_list, expected_output", [
    ([2, 7, 11, 15], (15, 11)),
    ([11, 7, 15, 2, 0, 13], (15, 13)),
    ([-33, -1, -44, -2, -55, -77], (-1, -2))
])
def test_find_max3(num_list, expected_output):
    assert find_top_max_numbers(num_list) == expected_output

