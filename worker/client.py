import requests

class Client:
    def __init__(self, cut_url, globo_play_url, video_path):
        self.cut_url = cut_url
        self.globo_play_url = globo_play_url
        self.video_path = video_path

    def post_cut(self, content, path):
        requests.post(path, data = content)
        # to_cut = { "video_path": path,
        #               "to_cut": content}
        # client.post(self.cut_url, data=to_cut) as resp:
        # resp.json()

    def get_cut(self, id):
        pass
        # client.get(f'{self.cut_url}/{id}') as resp:
        #     resp.content.read(chunk_size)

    def post_globo_play(self):
        pass
        # client.post(self.globo_play_url) as resp:
        #     resp.json()