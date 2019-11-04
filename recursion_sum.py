# функция суммирует числа списка используя рекурсию

list_elements = [2, 4, 6, 8, 3, 5, 7, 9, 1]


def sum_of_list(list_numbers):
    return 0 if not list_numbers else list_numbers.pop(0) + sum_of_list(list_numbers)


print(sum_of_list(list_elements))


def count_list(list_of_element):
    if not list_of_element:
        return 0
    else:
        index = list_of_element[0]
        result = index.pop()
        return result


print('count_list', count_list([2, 4, 6, 8, 3, 5, 7, 9, 1]))

lists = [2, 4, 6, 8, 3, 5, 7, 9, 1]
print(lists[0], lists[1])
print(lists.__len__())
