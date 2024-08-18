def create_synonym_dictionary(n):
    synonyms = {}

    for i in range(n):
        pair = input(f"Пара {i+1}: ").split(" — ")
        word1 = pair[0].strip().lower()
        word2 = pair[1].strip().lower()

        synonyms[word1] = word2
        synonyms[word2] = word1

    return synonyms

def find_synonym(synonyms):
    while True:
        word = input("Введите слово: ").strip().lower()
        if word in synonyms:
            print(f"Синоним: {synonyms[word].capitalize()}")
            break
        else:
            print("Такого слова в словаре нет. Попробуйте ещё раз.")

# Ввод данных
n = int(input("Введите количество пар слов: "))

# Создание словаря синонимов
synonyms = create_synonym_dictionary(n)

# Поиск синонима
find_synonym(synonyms)

