import socket

SOCKET_PATH = "hello.sock"


def main() -> None:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(SOCKET_PATH)

        name = input("Enter your name: ")

        client.sendall(name.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")

        print(f"Server says: {response}")


if __name__ == "__main__":
    main()
