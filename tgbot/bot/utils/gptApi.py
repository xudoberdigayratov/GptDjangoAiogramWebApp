import aiohttp


async def gpt_api(query):
    try:
        async with aiohttp.ClientSession() as session:
            prompt = {"gpt": [], "user": query}
            async with session.post(url="https://chat-gpt.hazex.workers.dev/", json=prompt) as response:
                data = await response.json()
                return data
    except Exception as e:
        return {
            "error": True,
            "message": "Method not allowed"
        }
