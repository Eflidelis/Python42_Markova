def compare_files(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1:
            lines1 = f1.readlines()
    except FileNotFoundError:
        print(f"Файл '{file1}' не найден")
        return

    try:
        with open(file2, 'r', encoding='utf-8') as f2:
            lines2 = f2.readlines()
    except FileNotFoundError:
        print(f"Файл '{file2}' не найден")
        return

    min_lines = min(len(lines1), len(lines2))

    for i in range(min_lines):
        line1 = lines1[i].strip()
        line2 = lines2[i].strip()

        if line1 != line2:
            print(f"Несовпадающая строка из файла 1 (строка {i + 1}): {line1}")
            print(f"Несовпадающая строка из файла 2 (строка {i + 1}): {line2}")

    if len(lines1) > min_lines:
        for i in range(min_lines, len(lines1)):
            print(f"Дополнительная строка из файла 1 (строка {i + 1}): {lines1[i].strip()}")

    if len(lines2) > min_lines:
        for i in range(min_lines, len(lines2)):
            print(f"Дополнительная строка из файла 2 (строка {i + 1}): {lines2[i].strip()}")


file1_path = 'file1.txt'
file2_path = 'file2.txt'

compare_files(file1_path, file2_path)
