def f2(n: int) -> int:
    return n * 2


def f1(n: int) -> int:
    new_n = f2(n)

    return new_n


if __name__ == "__main__":
    print(f1(10))
