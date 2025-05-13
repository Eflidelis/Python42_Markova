def replace_word_in_file(input_file, target_word, replacement_word):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace(target_word, replacement_word)

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Слово '{target_word}' было заменено на '{replacement_word}'.")

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")

input_file_path = 'input.txt'
target_word = input("Введите слово для замены: ")
replacement_word = input("Введите новое слово: ")

replace_word_in_file(input_file_path, target_word, replacement_word)
