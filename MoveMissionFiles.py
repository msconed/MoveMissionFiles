import os
import shutil
import json

def main():
    # Загружаем настройки из settings.json
    with open("settings.json") as f:
        settings = json.load(f)

    # Исходная директория
    source_dir = settings["source_dir"]

    # Список целевых директорий
    target_dirs = settings["target_dirs"]

    # Список файлов, которые не нужно копировать
    exclude_files = settings["exclude_files"]

    # Копируем содержимое
    for target_dir in target_dirs:
        copy_directory(source_dir, target_dir, exclude_files)

def copy_directory(source_dir, target_dir, exclude_files):
    # Создаем целевую директорию, если ее нет
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Перебираем все файлы и подпапки в исходной директории
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        # Проверяем, нужно ли копировать файл
        if item in exclude_files:
            continue

        # Копируем файл или подпапку
        if os.path.isfile(source_path):
            shutil.copy2(source_path, target_path)
        elif os.path.isdir(source_path):
            copy_directory(source_path, target_path, exclude_files)

if __name__ == "__main__":
    main()
