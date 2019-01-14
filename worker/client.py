import requests
import time
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s - %(message)s')

if not os.path.exists('worker/logs'):
    os.makedirs('worker/logs')

file_handler = logging.FileHandler('worker/logs/client.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
class Client:
    def __init__(self, cut_url, globo_play_url, video_path):
        self.cut_url = cut_url
        self.globo_play_url = globo_play_url
        self.video_path = video_path
        self.file_name = ""
        self.duration = "00:00:30"
        self.title = ""
        self.video_code = ""

    def content_info(self, content):
        video_info = content['to_cut']
        self.file_name = f'{video_info["reconcile_key"]}.mp4'
        self.duration = f'{video_info["duration"]}'
        self.title = f'{video_info["title"]}'

    def post_cut(self, content):
        path = { "video_path": self.video_path }
        content.update(path)
        r = requests.post(self.cut_url, params = content)
        logger.info(f'POST cut - title: {self.title} status:{r.status_code} -> {r.json()}')
        self.content_info(content)
        # Checa o retorno do POST e so envia o get quando a criação do job for bem sucedida
        if r.status_code == 201:
            # A api retorna a id do job de corte
            self.get_cut(r.json()['id'])
        return r


    def get_cut(self, id):
        r = requests.get(f'{self.cut_url}/{id}', stream = True )
        logger.info(f'GET cut title: {self.title} status:{r.status_code}')
        if r.status_code == 202:
            logger.info(f'GET cut title: {self.title} status:{r.status_code}, ainda processando...')
            time.sleep(10)
            self.get_cut(id)
        if r.status_code == 200:
            file_full_path = f'{self.video_path}/{self.file_name}'
            with open(file_full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk: 
                        f.write(chunk)
                logger.info(f'VIDEO DOWNLOAD {file_full_path}')
            self.post_globo_play(self.file_name)
        else:
            return r

    def post_globo_play(self, file_name):
        body = { "duration": self.duration, "title": self.title, "file_name": self.file_name}
        r = requests.post(self.globo_play_url, params = body)
