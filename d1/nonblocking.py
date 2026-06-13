import random
import threading
import time


def generate_number(name: str) -> int:
    random_num = random.randint(0, 100)
    print(f"{name} generated number: {random_num}")

    # time.sleep(1)

    return random_num


def fun(name: str) -> None:
    print(f"{name} arrived")
    # time.sleep(1)

    num = generate_number(name)
    print(f"{name} received number: {num}")
    # time.sleep(1)

    print(f"{name} left")


if __name__ == "__main__":
    t1 = threading.Thread(target=fun, args=("Tony Stark",))
    t2 = threading.Thread(target=fun, args=("Iron Man",))
    t3 = threading.Thread(target=fun, args=("Someone else",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
