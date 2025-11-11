import sys
import random
import string
import asyncio
from concurrent.futures import ProcessPoolExecutor
from aiofiles import open as async_open


# Синхронная функция генерации строки (используется в процессах)
def generate_random_string():
    characters = string.ascii_letters + ' '
    length = random.randint(2, 100)
    return ''.join(random.choice(characters) for _ in range(length))


# Асинхронная функция записи строки в файл
async def write_to_file(file_path, lines):
    async with async_open(file_path, mode="a", encoding="utf-8") as f:
        for line in lines:
            await f.write(line + '\\n')


# Основная асинхронная функция
async def main(file_path, string_count):
    executor = ProcessPoolExecutor(max_workers=4)  # Количество рабочих процессов

    # Генерация строк в отдельных процессах
    strings = await asyncio.get_running_loop().run_in_executor(
        executor,
        lambda: [generate_random_string() for _ in range(string_count)]
    )

    # Разделяем строки на пакеты для параллельного написания
    chunk_size = max(len(strings) // 4, 1)
    chunks = [strings[i:i+chunk_size] for i in range(0, len(strings), chunk_size)]

    # Запись пакетов строк в файл параллельно
    await asyncio.gather(*(write_to_file(file_path, chunk) for chunk in chunks))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Необходимо передать два аргумента: путь к файлу и количество строк.")

    file_path = sys.argv[1]
    string_count = int(sys.argv[2])

    asyncio.run(main(file_path, string_count))
