# chatgpt

import asyncio
import requests


async def get_url(url):
    with requests.Session() as session:
        response = await loop.run_in_executor(None, session.get, url)
        return response.text


async def main():
    url = "https://www.google.com"
    response_text = await get_url(url)
    print(response_text)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
