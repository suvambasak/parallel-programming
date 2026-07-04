import math
import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
from threading import Thread


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
    print("[count_primes] __main__ ID:", os.getpid())

    # for i in range(10):
    #     count_primes(1000000)

    # threads = []
    # for i in range(10):
    #     t = Thread(target=count_primes, args=(1000000,))
    #     threads.append(t)
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()

    # processes = []
    # for i in range(10):
    #     p = Process(target=count_primes, args=(1000000,))
    #     processes.append(p)
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()

    # executor = ProcessPoolExecutor()
    # for i in range(10):
    #     executor.submit(count_primes, 1000000)
    # executor.shutdown()

    with ProcessPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            executor.submit(count_primes, 1000000)
