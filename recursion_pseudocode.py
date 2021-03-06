"""
Рекурсия
Допустим вы разбираете чулан своей бабушки и натыкаетесь на загадочный запертый чемодан.
Бабушка говорит, что ключ к чемодану, скорее всего, лежит в коробке.
В коробке лежат другие коробки, а в них лежат маленькие коробочки.
Ключ находится где-то там. Какой алгоритм поиска предложите вы?

#################################################################################
Первый метод решения перебором:
1. Сложить все коробки в кучу.
2. Взять коробку и открыть.
3. Если внутри лежит коробка, добавить ее в кучу для последующего поиска.
4. Если внутри лежит ключ, поиск завершен!
5. Повторить.

# Псевдо-код:
# Пока куча коробок не пуста, взять очередную коробку и проверить её содержимое

def look_for_key1(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('found the key')

################################################################################
Второй метод решения рекурсией:
1. Просмотреть содержимое коробки.
2. Если вы найдете коробку, вернуться к шагу 1
3. Если вы найдете ключ, поиск закончен.


# Псевдо-код:
# Рекурсией называется вызов функцией самой себя

def look_for_key2(box):
    for item in box:
        if item.is_a_box():
            look_for_key2(item)     # <--- РЕКУРСИЯ
        elif item.is_a_key():
            print('found the key')

"""