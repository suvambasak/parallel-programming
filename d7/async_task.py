import asyncio
import time


async def task(idx: int) -> bool:

    print(f"START TASK {idx}")
    # time.sleep(1)
    await asyncio.sleep(1)
    print(f"END TASK {idx}")

    return True


async def main() -> None:

    # for i in range(10):
    #     task(i)

    # tasks = []
    # for idx in range(10):
    #     t = asyncio.create_task(task(idx))
    #     tasks.append(t)

    # for t in tasks:
    #     status = await t
    #     print(f"Task status: {status}")

    await asyncio.gather(*[task(idx) for idx in range(10)])


if __name__ == "__main__":
    # main()
    asyncio.run(main())
