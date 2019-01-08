import time
import sys
import logging
import os
from dir_event_handler import DirEventHandler
from watchdog.observers import Observer
from text_parser import TextParser


if __name__ == '__main__':
    # o diretorio à ser observador será passado como argumento ao rodar o script, ou o 
    # script sempre vai observar o proprio diretorio onde ele esta localizado
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s- %(message)s')
    file_handler = logging.FileHandler('logs/errors.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(file_handler)
    observer = Observer() # instancia uma classe do observador do watchdog
    tp = TextParser() # instancia a classe do parser
    event_handler = DirEventHandler(tp, path) # cria o gerenciador de eventos
    # seta o observar para usar o gerenciador de eventos no diretorio
    observer.schedule(event_handler, path = path)
    observer.start()
    print(f'Iniciando a observação do diretório -> {path}')
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()