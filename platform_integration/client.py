import aiohttp
import time

class Client:
    def __init__(self, cut_url, globo_play_url, video_path):
        self.cut_url = cut_url
        self.globo_play_url = globo_play_url
        self.video_path = video_path

    async def post_cut(self, client, content, path):
        to_cut = { "video_path": path,
                      "to_cut": content}
        async with client.post(self.cut_url, data=to_cut) as resp:
            return await resp.json()

    async def get_cut(self, client, id):
        async with client.get(f'{self.cut_url}/{id}') as resp:
            return await resp.content.read(chunk_size)

    async def post_globo_play(self, client):
        async with client.post(self.globo_play_url) as resp:
            return await resp.json()

    async def request(self, content):
        async with aiohttp.ClientSession() as client:
            post_cut = await self.post_cut(client, content, self.video_path)
            # cut_id = post_cut.json(id)
            # get_cut = await self.get_cut(client, cut_id)
            return(post_cut)