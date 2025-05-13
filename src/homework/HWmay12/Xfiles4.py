def find_longest_line_length(input_file):
    try:
        max_length = 0

        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line_length = len(line.rstrip('\n'))
                if line_length > max_length:
                    max_length = line_length

        return max_length

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
        return None

input_file_path = 'input.txt'

longest_length = find_longest_line_length(input_file_path)
if longest_length is not None:
    print(f"Длина самой длинной строки: {longest_length}")
