import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.ws_connect("ws://localhost:8765/") as ws:
            n = 0
            print(f"Sending 'hello{n}'")
            await ws.send_str(f"hello{n}")
            async for msg in ws:
                print(f"Received '{ msg.data }'")

                print(f"Sending 'hello{n}'")
                await ws.send_str(f"hello{n}")

                n += 1
                if n == 10:
                    return


asyncio.run(main())
