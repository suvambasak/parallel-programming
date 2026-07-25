import math
import os
from concurrent.futures import InterpreterPoolExecutor


def count_primes(limit: int) -> int:
    print("[count_primes] Process ID:", os.getpid())

    count = 0
    for n in range(2, limit + 1):
        is_prime = True
        sqrt_n = int(math.sqrt(n))

        for divisor in range(2, sqrt_n + 1):
            if n % divisor == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count


if __name__ == "__main__":
    with InterpreterPoolExecutor() as executor:
        for i in range(10):
            executor.submit(count_primes, 1000000)
