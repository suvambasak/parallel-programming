import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock: socket.socket) -> None:
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            print(f"\nServer: says {message}")
        except Exception as e:
            print(f"Error: {e}")
            break


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        receiver = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True,
        )
        receiver.start()

        while True:
            message = input("Enter message: ")
            client.sendall(message.encode("utf-8"))

            if message.upper() == "EXIT":
                client.close()
                print("Client closed.")
                break

        receiver.join()


if __name__ == "__main__":
    main()
