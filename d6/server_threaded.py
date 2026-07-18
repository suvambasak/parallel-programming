import socket
import threading

HOST = "0.0.0.0"
PORT = 5000


def handle_client(conn: socket.socket, addr: tuple) -> None:
    print(f"Connected by {addr}")
    while True:
        message = conn.recv(1024).decode("utf-8")
        print(f"Client says: {message}")

        if message.upper() == "EXIT":
            conn.close()
            break

        response = f"Hello {message}"
        conn.sendall(response.encode("utf-8"))


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()

            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()
