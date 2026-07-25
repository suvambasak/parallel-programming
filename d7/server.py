import os
import socket

SOCKET_PATH = "hello.sock"


def main() -> None:

    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(SOCKET_PATH)
        server.listen(1)
        print(f"Server listening on {SOCKET_PATH}")

        conn, _ = server.accept()

        with conn:
            name = conn.recv(1024).decode("utf-8")
            print(f"Received: {name}")

            message = f"Hello {name}"
            conn.sendall(message.encode("utf-8"))

        print("Connection closed.")

    os.remove(SOCKET_PATH)


if __name__ == "__main__":
    main()
