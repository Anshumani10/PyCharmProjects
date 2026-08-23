import asyncio
import time


def task(name):
    print("starting name is :", name)
    time.sleep(2)
    print("ending name is :", name)

#task("Rahul")
#task("Shetty")

print("*************************")

async def task(name):
        print("starting name is :", name)
        await asyncio.sleep(2)
        print("ending name is :", name)


async def main():
    await asyncio.gather(task("Rahul"), task("Shetty"))

asyncio.run(main())

