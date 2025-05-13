def analyze_file(input_file, output_file):
    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    russian_vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    russian_consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    latin_vowels = "aeiouyAEIOUY"
    latin_consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line_count += 1
                char_count += len(line)

                for char in line:
                    if char in russian_vowels or char in latin_vowels:
                        vowel_count += 1
                    elif char in russian_consonants or char in latin_consonants:
                        consonant_count += 1
                    elif char.isdigit():
                        digit_count += 1

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден")
        return

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Количество символов: {char_count}\n")
        f.write(f"Количество строк: {line_count}\n")
        f.write(f"Количество гласных букв: {vowel_count}\n")
        f.write(f"Количество согласных букв: {consonant_count}\n")
        f.write(f"Количество цифр: {digit_count}\n")

input_file_path = 'input.txt'
output_file_path = 'output.txt'

analyze_file(input_file_path, output_file_path)
