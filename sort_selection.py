"""
Сортировка массива по возрастанию
"""


def find_smallest(arr):
    smallest = arr[0]       # для хранения наименьшего значения
    smallest_index = 0      # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """ Сортировка выбором """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    print(new_arr, end=" - ")
    return new_arr


def test_selection_sort(arr):
    print("Тестируем:", selection_sort.__doc__)
    print("test_case #1: ", end="")
    a = [5, 3, 6, 8, 1, 4, 2, 10]
    a_sorted = [1, 2, 3, 4, 5, 6, 8, 10]
    print("OK" if selection_sort(a) == a_sorted else "Fail")  # тернарный условный оператор


if __name__ == "__main__":
    test_selection_sort(selection_sort)
