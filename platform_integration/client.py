import aiohttp

class Client():
    async def post_cut(self, client):
        async with client.post('http://google.com') as resp:
            assert resp.status == 200
            return await resp.text()

    async def get_cut(self, client):
        async with client.get('http://python.org') as resp:
            assert resp.status == 200
            return await resp.text()

    async def post_globo_play(self, client):
        async with client.post('http://pudim.com.br') as resp:
            assert resp.status == 200
            return await resp.text()

    async def main(self):
        async with aiohttp.ClientSession() as client:
            html = await self.get_cut(client)
            print(html)

    #POST videos a serem cortados - api/v1/corte
    # - { "cuts" : [
        # { "start_time": "timecode",
        # "end_time": "timecode",
        # "path": "path arquivo a ser salvo" }
        #  ]
    # }
    # GET  status do corte e video api/v1/corte/:id a cada x tempo

    # POST para api globo-play