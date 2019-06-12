import asyncio


@asyncio.coroutine #通过这个装饰器装饰
def func1():
    print('before...func1......')
    # 这里必须用yield from，并且这里必须是asyncio.sleep不能是time.sleep
    yield from asyncio.sleep(2)
    print('end...func1......')


tasks = [func1(), func1()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()