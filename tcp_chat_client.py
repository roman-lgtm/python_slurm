import socket
import threading

server = "127.0.0.1", 12312
name = input(f'Введите ваше имя:')

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server)

socket.send(name.encode('UTF-8'))

def read_socket():
   try:
       while True:
           data = socket.recv(1024)
           if not data:
               break
           print(data.decode('UTF-8'))
   except Exception as e:
       print(f'Произошла ошибка при приеме сообщения {e}')

receiver_thread = threading.Thread(target=read_socket())
receiver_thread.daemon = True  # Завершаем поток вместе с программой
receiver_thread.start()

try:
    while True:
        message = input()
        socket.send(message.encode('UTF-8'))
except KeyboardInterrupt:
    print("\\nОшибка при попытке отправить")
finally:
    # Закрываем сокет
    socket.close()
