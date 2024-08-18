def can_form_palindrome(s):
    # Словарь для подсчета частоты символов
    char_count = {}

    # Подсчет вхождений каждого символа
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Подсчет количества символов с нечетным количеством вхождений
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Если нечетное количество символов больше одного, палиндром невозможен
    return odd_count <= 1

# Ввод строки пользователем
user_input = input("Введите строку: ")

# Проверка возможности создать палиндром
if can_form_palindrome(user_input):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
