def count_word_in_file(input_file, target_word):
    try:
        word_count = 0

        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                word_count += words.count(target_word)

        return word_count

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
        return None

input_file_path = 'input.txt'
target_word = input("Введите слово для поиска: ")

count = count_word_in_file(input_file_path, target_word)
if count is not None:
    print(f"Слово '{target_word}' встречается {count} раз(а) в файле.")
