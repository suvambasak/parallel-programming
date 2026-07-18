import socket

HOST = "0.0.0.0"
PORT = 5000


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server.accept()
        print(f"Connected by {addr}")

        with conn:
            name = conn.recv(1024).decode("utf-8")
            print(f"Received: {name}")

            message = f"Hello {name}"
            conn.sendall(message.encode("utf-8"))

        print("Connection closed.")


if __name__ == "__main__":
    main()
