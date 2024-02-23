import os
import sys
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO, encoding='utf-8', filemode='w')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])


def get_file_info(file_path):
    try:
        files_info = []
        for item in os.listdir(file_path):
            full_path = os.path.join(file_path, item)
            name, extension = os.path.splitext(item)
            is_directory = os.path.isdir(full_path)
            parent_dir = os.path.basename(os.path.dirname(full_path))
            file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_dir=parent_dir)
            files_info.append(file_info)
            logging.info(f'Обрабатывается файл: {item}')
        return files_info
    except Exception as e:
        logging.error(f'Ошибка обработки {file_path}: {str(e)}')
        return []


def main():
    parser = argparse.ArgumentParser(description='Собираю информацию о файлах и папках.')
    parser.add_argument('directory', help='Папка для обработки')
    args = parser.parse_args()

    directory_path = os.path.abspath(args.directory)

    if not os.path.exists(directory_path):
        print(f'Папка {directory_path} не существует.')
        sys.exit(1)

    files_info = get_file_info(directory_path)

    with open('file_info.txt', 'w', encoding='UTF-8') as f:
        for file_info in files_info:
            f.write(
                f"Имя файла: {file_info.name}\nРасширение: {file_info.extension}\nЯвляется папкой: {file_info.is_directory}\nРодительская папка: {file_info.parent_dir}\n\n")

    print("Информация о файлах сохранена в file_info.txt.")


if __name__ == "__main__":
    main()
