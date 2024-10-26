import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    command, filename = request.split(' ', 1)

    if command == 'PUT':
        print(f"Receiving file: {filename}")
        with open(filename, 'wb') as f:
            while (chunk := client_socket.recv(1024)):
                if not chunk:
                    break
                f.write(chunk)
        print(f"File {filename} received and saved.")
    client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9997))
    server.listen(5)

    while True:
        client_socket, _ = server.accept()
        handle_client(client_socket)


if __name__ == "__main__":
    main()
