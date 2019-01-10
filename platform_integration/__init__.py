from .text_parser import TextParser
from .dir_event_handler import DirEventHandler
from .client import Client
from watchdog.observers import Observer
import asyncio
import sys
import os

# o diretorio à ser observador será passado como argumento ao rodar o script, ou o 
# script sempre vai observar o proprio diretorio onde ele esta localizado
path = sys.argv[1] if len(sys.argv) > 1 else '.'
# seta o observer para usar o gerenciador de eventos no diretorio
observer = Observer() # instancia uma classe do observador do watchdog
tp = TextParser() # instancia a classe do parser
cut_url = 'https://jsonplaceholder.typicode.com/posts' # api de exemplo para testes
globo_play_url = 'https://jsonplaceholder.typicode.com/posts'
video_path = "path/to/save/video"
client = Client(cut_url, globo_play_url, video_path) # instancia a class do http client
# cria o gerenciador de eventos
event_handler = DirEventHandler(tp, path, client)