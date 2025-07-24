import threading
import os


def find_files_with_word(dir_path, word, output_file):
    found_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if word in file:
                found_files.append(os.path.join(root, file))
    with open(output_file, 'w') as f:
        for file in found_files:
            f.write(f"{file}\n")
    print(f"Найдено файлов с словом '{word}': {len(found_files)}")


def remove_prohibited_words(input_file, output_file, prohibited_words_file):
    with open(prohibited_words_file, 'r') as f:
        prohibited_words = set(word.strip() for word in f)
    with open(input_file, 'r') as f:
        contents = f.read()
    for word in prohibited_words:
        contents = contents.replace(word, "")
    with open(output_file, 'w') as f:
        f.write(contents)
    print("Запрещенные слова удалены.")


def main(dir_path, word):
    output_file = 'found_files.txt'
    find_thread = threading.Thread(target=find_files_with_word, args=(dir_path, word, output_file))
    remove_thread = threading.Thread(target=remove_prohibited_words, args=(output_file, 'final_output.txt', 'prohibited_words.txt'))

    find_thread.start()
    find_thread.join()

    remove_thread.start()
    remove_thread.join()


if __name__ == "__main__":
    dir_path = input("Введите путь к существующей директории: ")
    search_word = input("Введите слово для поиска: ")
    main(dir_path, search_word)
