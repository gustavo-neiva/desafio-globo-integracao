from flask import Flask
from platform_integration.text_parser import TextParser
from platform_integration.dir_event_handler import DirEventHandler
from watchdog.observers import Observer
from queue import Queue
import logging
import sys
import os
import threading

app = Flask(__name__)
# o diretorio à ser observador será passado como argumento ao rodar o script, ou o 
# script sempre vai observar o proprio diretorio onde ele esta localizado
# seta o observar para usar o gerenciador de eventos no diretorio
path = sys.argv[1] if len(sys.argv) > 1 else '.'
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s- %(message)s')
# file_handler = logging.FileHandler('platform_integration/logs/errors.log')
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.ERROR)
# logger.addHandler(file_handler)
observer = Observer() # instancia uma classe do observador do watchdog
tp = TextParser() # instancia a classe do parser
event_handler = DirEventHandler(tp, path) # cria o gerenciador de eventos