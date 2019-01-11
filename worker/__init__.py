from .client import Client
import pika

cut_url = 'https://jsonplaceholder.typicode.com/posts' # api de exemplo para testes
globo_play_url = 'https://jsonplaceholder.typicode.com/posts'
video_path = "path/to/save/video"
client = Client(cut_url, globo_play_url, video_path) # instancia a class do http client
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='to_cut')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                        queue='to_cut',
                        no_ack=True)
    print(' [*] Esperando mensagens... Para sair pressione CTRL+C')
    channel.start_consuming()