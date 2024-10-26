import socket


def upload_file(client_socket, filename):
    try:
        print(f"Uploading file: {filename}")
        client_socket.send(f'PUT {filename}'.encode('utf-8'))
        with open(filename, 'rb') as f:
            while (chunk := f.read(1024)):
                client_socket.send(chunk)
        client_socket.send(b'')  # End of file
        print(f"File {filename} uploaded successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def download_file(client_socket, filename):
    filename = filename.strip()  # Remove any leading or trailing spaces
    client_socket.send(f'GET {filename}'.encode('utf-8'))

    with open(filename, 'wb') as f:
        while (chunk := client_socket.recv(1024)):
            if not chunk:
                break
            f.write(chunk)
    print(f"File {filename} downloaded successfully.")


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9992))

    while True:
        command = input('Enter command (upload/download/quit): ')
        if command == 'upload':
            filename = input('Enter filename to upload (relative path): ')
            upload_file(client, filename)
        elif command == 'download':
            filename = input('Enter filename to download (relative path): ')
            download_file(client, filename)
        elif command == 'quit':
            break
        else:
            print('Invalid command')

    client.close()


if __name__ == "__main__":
    main()
