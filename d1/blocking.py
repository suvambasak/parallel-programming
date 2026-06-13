import random
import time


def generate_number(name: str) -> int:
    random_num = random.randint(0, 100)
    print(f"{name} generated number: {random_num}")

    time.sleep(1)

    return random_num


def fun(name: str) -> None:
    print(f"START: fun by {name}")
    time.sleep(1)

    num = generate_number(name)
    print(f"{name} received number: {num}")
    time.sleep(1)

    print(f"END: fun by {name}")


if __name__ == "__main__":
    fun("Tony Stark")
    fun("Iron Man")
