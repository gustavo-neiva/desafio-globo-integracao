from .text_parser import TextParser
from .dir_event_handler import DirEventHandler
from watchdog.observers import Observer
import pika
import sys
import os

# o diretorio à ser observador será passado como argumento ao rodar o script, ou o 
# script sempre vai observar o proprio diretorio onde ele esta localizado
path = sys.argv[1] if len(sys.argv) > 1 else '.'
# seta o observer para usar o gerenciador de eventos no diretorio
observer = Observer() # instancia uma classe do observador do watchdog
tp = TextParser() # instancia a classe do parser
# cria o gerenciador de eventos
event_handler = DirEventHandler(tp, path)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()