from .client import Client
import json
import pika
import sys

cut_url = 'https://httpbin.org/' # api de exemplo para testes
globo_play_url = 'https://httpbin.org/'
default_path = "/home/storm000634/code/luizgzn/desafio-globo-integracao/tests/videos"
video_path = sys.argv[1] if len(sys.argv) > 1 else default_path
client = Client(cut_url, globo_play_url, video_path) # instancia a class do http client
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='to_cut')

    def callback(ch, method, properties, body):
        print(" [x] Recebido %r" % body)
        json_body = json.loads(body)
        client.post_cut(json_body)

    channel.basic_consume(callback,
                        queue='to_cut',
                        no_ack=True)
    print(' [*] Esperando mensagens... Para sair pressione CTRL+C')
    channel.start_consuming()