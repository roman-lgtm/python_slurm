import sys
import os
from homework import is_valid_umnoe


def read_file_and_check_skobki(file_path):
    try:
        with open(file_path,encoding='utf-8') as f:
            content = ''.join(f.readlines())
            if is_valid_umnoe(content):
                result_message = ': Валидно'
            else:
                result_message = ': Ошибка'
            with open('result.txt', 'a', encoding='utf-8') as result_file:
                result_file.write(f'{file_path}{result_message}\n')
    except Exception as e:
        print(f"Произошла ошибка при обработке файла {file_path}: {e}")


def read_dir_and_check_skobki(start_directory):
    for current_dir, sub_dirs, files in os.walk(start_directory):
        for filename in files:
            full_file_path = os.path.join(current_dir, filename)
            read_file_and_check_skobki(full_file_path)


def is_valid_in_file():
    file = sys.argv[1]
    if os.path.isfile(file):
        read_file_and_check_skobki(file)
    elif os.path.isdir(file):
        read_dir_and_check_skobki(file)