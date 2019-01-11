import os
import pika
import json
from watchdog.events import FileSystemEventHandler

class DirEventHandler(FileSystemEventHandler):
    def __init__(self, tp, path):
        self.tp = tp
        self.path = path

    def process(self, event):      
        # o conteudo informativo começa a partir da linha 7
        # como cada novo arquivo contem as mesmas linhas do arquvio anterior mais as novas informaçoes
        # a linha pelo qual o parser deve iniciar é igual ao número de linhas do arquivo
        # anterior - 1 para deixar a contagem certa

        # remover arquivos ocultos da observacao e contar apenas os .txt
        list_dir = [f for f in os.listdir(self.path) if not f.startswith('.') and f.endswith('.txt')]
        if len(list_dir) > 1:
            forehand_file_path = f'{self.path}/{sorted(list_dir)[-2]}'
            forehand_file_lines = self.tp.count_lines(forehand_file_path)
            start_line = forehand_file_lines - 1
        else:
            start_line = 7
        parsed_content = self.tp.parse_content(event.src_path, start_line)
        for content in parsed_content:
            dictionary = { "to_cut": content }
            self.send_message(dictionary)
        
    def on_created(self, event): # quando o arquivo for criado no diretorio
        self.process(event)

    def send_message(self, content):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='to_cut')
        message = json.dumps(content)
        channel.basic_publish(exchange='',
                            routing_key='to_cut',
                            body=message)
        print(f"[x] Eviado - {message}")
        connection.close()