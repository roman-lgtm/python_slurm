import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(('127.0.0.1', 12312))
tcp_socket.listen()

print(f'Server is successfully started')
users = []

try:
    while True:
        # Принятие нового подключения
        client_socket, addr = tcp_socket.accept()

        users.append(client_socket)
        print(f'New connection from {addr}')

        # Получаем данные от клиента
        data = client_socket.recv(1024)
        message = data.decode('utf-8')
        print(f'Message from [{addr}]: {message}')

        # Отправляем сообщение другим клиентам
        for user in users:
            if user != client_socket:
                try:
                    user.sendall(data)
                except Exception as e:
                    print(f"Error sending to {user.getpeername()}: {e}")
except KeyboardInterrupt:
    print("\\nShutting down server...")
finally:
    # Закрываем все клиентские сокеты
    for client in users:
        client.close()
    tcp_socket.close()