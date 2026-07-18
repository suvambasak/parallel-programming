import socket

HOST = "172.27.18.1"
PORT = 5000


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        name = input("Enter your name: ")
        client.sendall(name.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")

        print(f"Server says: {response}")


if __name__ == "__main__":
    main()
