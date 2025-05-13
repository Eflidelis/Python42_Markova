def remove_last_line(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) > 0:
            lines = lines[:-1]

        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")

input_file_path = 'input.txt'
output_file_path = 'output.txt'

remove_last_line(input_file_path, output_file_path)
