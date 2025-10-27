import sys
import random
import string

def random_string():
    characters = string.ascii_letters + ' '
    length = random.randint(2, 100)
    selected_chars = []
    for i in range(length):
        select_char = random.choice(characters)
        selected_chars.append(select_char)
    result_str = ''.join(selected_chars)
    return result_str

def random_generator_out_file():
    file_path = sys.argv[1]
    string_count = int(sys.argv[2])
    while string_count > 0:
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f'{random_string()}\n')
                string_count -= 1
        except Exception as e:
            print(f"Произошла ошибка при обработке файла {file_path}: {e}")


random_generator_out_file()