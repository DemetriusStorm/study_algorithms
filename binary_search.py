"""
binary search
Бинарный поиск работает только в том случае, если список отсортирован.
Например, имена в телефонной книге хранятся в алфавитном порядке, и вы
можете воспользоваться бинарным поиском. А что произойдёт, если имена
не будут отсортированы?..
"""


def binary_search(list_in, item):
    count_iter = 0
    low = 0                      # В переменных low и high хранятся границы
    high = len(list_in) - 1      # той части списка, в которой выполняется поиск
    while low <= high:           # Пока эта часть не сократится до одного элемента..
        mid = (low + high) // 2  # ...проверяем средний элемент (отбрасываем дробную часть)
        print('Середина списка за текущую итерацию; mid =', mid)
        guess = list_in[mid]
        print('Нашли число? guess =', guess)
        if guess == item:        # Значение найдено
            return 'Нашли, у вашего числа {}, индекс {}. Всего итераций (проверок): {}'.format(item, mid, count_iter)
        elif guess > item:       # Много
            high = mid - 1
            count_iter += 1
        else:                    # Мало
            low = mid + 1
            count_iter += 1
        # print('Всего итерация:', count)
    return 'Загаданное число отсутствует в списке. Всего итераций (проверок): {}'.format(count_iter)  # Значение не существует


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(my_list, 7))

"""
Упраженение 1.1

Имеется отсортированный список из 128 имён, и вы ищите в нем значение методом 
бинарного поиска. Какое максимальное кол-во проверок для этого может потребоваться?
Ответ: log_2(128) = 6
========================================================================================
Упражнение 1.2
Предположим, размер списка увеличился вдвое. Как изменится максимальное кол-во проверок?

Ответ: +1 к предыдущем, log_2(256) = 7 
"""