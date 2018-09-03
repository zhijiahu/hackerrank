
import asyncio
import aiohttp


async def main(loop):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:9001', data='test') as resp:
            print(await resp.text())


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
loop.close()
