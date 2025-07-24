import threading
import os
import shutil


def copy_directory(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Скопировано: {s} в {d}")


def main(src, dst):
    copy_thread = threading.Thread(target=copy_directory, args=(src, dst))
    copy_thread.start()
    copy_thread.join()
    print("Копирование завершено.")


if __name__ == "__main__":
    src_directory = input("Введите путь к существующей директории: ")
    dst_directory = input("Введите путь к новой директории: ")
    main(src_directory, dst_directory)
