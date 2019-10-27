def sort_selection(arr):
    """ сортировка списка А выбором """
    n = len(arr)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]


def test_sort(sort_algorithm):
    print("Тестируем:", sort_algorithm.__doc__)
    print("test_case #1: ", end="")
    a = [5, 3, 6, 8, 1, 4, 2, 10]
    a_sorted = [1, 2, 3, 4, 5, 6, 8, 10]
    sort_algorithm(a)
    print("OK" if a == a_sorted else "Fail")  # тернарный условный оператор


if __name__ == "__main__":
    test_sort(sort_selection)

