from .text_parser import TextParser
from .dir_event_handler import DirEventHandler
from .client import Client
from watchdog.observers import Observer
import asyncio
import sys
import os

# o diretorio à ser observador será passado como argumento ao rodar o script, ou o 
# script sempre vai observar o proprio diretorio onde ele esta localizado
# seta o observar para usar o gerenciador de eventos no diretorio
path = sys.argv[1] if len(sys.argv) > 1 else '.'
observer = Observer() # instancia uma classe do observador do watchdog
tp = TextParser() # instancia a classe do parser
c = Client()
event_handler = DirEventHandler(tp, path, c) # cria o gerenciador de eventos