from .worker import Client
import json
import pika
import sys

cut_url = 'https://sample-videos.com/video123/mp4/480/big_buck_bunny_480p_30mb.mp4' # api de exemplo para download de video
globo_play_url = 'https://httpbin.org/post'
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
        client.process(json_body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(callback,
                        queue='to_cut')
    print(' [*] Esperando mensagens... Para sair pressione CTRL+C')
    channel.start_consuming()