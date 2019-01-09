import aiohttp

class Client():
    def __init__(self, cut_url, globo_play_url):
        self.cut_url = cut_url
        self.globo_play_url = globo_play_url
        self.

    async def post_cut(self, client, content):
        async with client.post(self.cut_url) as resp:
            assert resp.status == 200
            return await resp.json()

    async def get_cut(self, client):
        async with client.get(self.cut_url) as resp:
            assert resp.status == 200
            return await resp.json()

    async def post_globo_play(self, client):
        async with client.post(self.globo_play_url) as resp:
            assert resp.status == 200
            return await resp.json()

    async def main(self, content):
        async with aiohttp.ClientSession() as client:
            html = await self.get_cut(client)
            print(html[1])