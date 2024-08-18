
from collections import defaultdict

def create_frequency_dict(text):
    frequency_dict = {}
    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

def invert_frequency_dict(frequency_dict):
    inverted_dict = defaultdict(list)
    for char, frequency in frequency_dict.items():
        inverted_dict[frequency].append(char)
    return inverted_dict

def print_dict(d, title):
    print(f"{title}:")
    for key, value in d.items():
        print(f"{key}: {value}")

# Ввод текста
text = input("Введите текст: ")

# Создание оригинального словаря частот
frequency_dict = create_frequency_dict(text)

# Инвертирование словаря частот
inverted_dict = invert_frequency_dict(frequency_dict)

# Вывод оригинального и инвертированного словарей
print_dict(frequency_dict, "Оригинальный словарь частот")
print_dict(inverted_dict, "Инвертированный словарь частот")
