import requests
import time
import logging
import os
import sys

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
        self.duration = ""
        self.title = ""
        self.video_code = ""

    def content_info(self, content):
        video_info = content['to_cut']
        self.file_name = f'{video_info["reconcile_key"]}.mp4'
        self.duration = f'{video_info["duration"]}'
        self.title = f'{video_info["title"]}'

    def post_cut(self, content):
        # Estou utiliznado o url de teste para o post, mas idealmente a API de corte teria 
        # um endpoint 'api/v1/corte' que aceitaria um POST e que retorniaria a id do corte 
        # no corpo da resposta, dai com essa id eu faria um GET para 'api/v1/corte/:id'
        # mas para testar estou usando url diferentes
        r = requests.post(self.globo_play_url, data = content)
        logger.info(f'POST cut - title: {self.title} status:{r.status_code} -> {r.json()}')
        return r
        
    def get_cut(self, id):
        # Utilizei uma url para testar o download do video, porem como comentado acima 
        # idealmente eu adicionaria apenas a id ao endpoint de corte
        # r = requests.get(f'{self.cut_url}/{id}', stream = True )
        r = requests.get(self.cut_url, stream = True )
        logger.info(f'GET cut title: {self.title} status:{r.status_code}')
        return r

    def post_globo_play(self, file_name):
        body = { "duration": self.duration, "title": self.title, "file_name": self.file_name}
        r = requests.post(self.globo_play_url, data = body)
        return r

    def download_file(self, response):
        file_full_path = f'{self.video_path}/{self.file_name}'
        with open(file_full_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024): 
                if chunk: 
                    f.write(chunk)
            logger.info(f'VIDEO DOWNLOAD {file_full_path}')
        self.post_globo_play(self.file_name)

    def control_get_cut(self, id):
        try:
            r = self.get_cut(id)
            r.raise_for_status()
            if r.status_code == 200:
                self.download_file(r)
            elif r.status_code == 202:
                logger.info(f'GET cut title: {self.title} status:{r.status_code}, ainda processando...')
                time.sleep(10)
                self.get_cut(id)
        except requests.exceptions.HTTPError as err:
            logger.error(err)
            # sys.exit(1)        

    def control_post_cut(self, content):
        self.content_info(content)
        # Checa o retorno do POST e so envia o get quando a criação do job for bem sucedida
        try:
            r = self.post_cut(content)
            r.raise_for_status()
            json = r.json()
            if 'id' in json:
                id_corte = json['id']
            else:
                id_corte = 1
            self.control_get_cut(id_corte)
        except requests.exceptions.HTTPError as err:
            logger.error(err)
            # sys.exit(1)


    def process(self, content):
        path = { "video_path": self.video_path }
        content.update(path)
        self.control_post_cut(content)
