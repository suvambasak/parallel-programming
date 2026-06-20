import time
from threading import Thread

current_balance = 0.0


def transfer(amount: float) -> None:
    "Simulates a transfer of `amount` from the current balance."

    # Validate the transaction
    time.sleep(0.000001)

    # Get the current balance
    time.sleep(0.000001)
    global current_balance

    updated_balance = current_balance + amount

    # Debit the current balance
    time.sleep(0.000001)

    # Credit the updated balance
    time.sleep(0.000001)
    current_balance = updated_balance


if __name__ == "__main__":
    transations: list[Thread] = []

    for _ in range(10000):
        transation = Thread(target=transfer, args=(1.0,))
        transations.append(transation)

    for transation in transations:
        transation.start()

    for transation in transations:
        transation.join()

    print(f"Final balance value: {current_balance}")
