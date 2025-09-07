import asyncio

async def do_something(wait_time):
    print("Doing something", wait_time)
    await asyncio.sleep(wait_time)
    print("Done something", wait_time)
    return "Done something" + str(wait_time)

async def do_something_gather():
    result = await asyncio.gather(do_something(1), do_something(2), do_something(3))    
    return result 
    # await do_something(1)
    # await do_something(2)
    # await do_something(3)

result = asyncio.run(do_something_gather())
print(result)