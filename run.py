import time
import sys
from dir_event_handler import DirEventHandler
from watchdog.observers import Observer
from text_parser import TextParser


if __name__ == '__main__':
    # o diretorio à ser observador será passadom como argumento ao rodar o script, ou o 
    # script sempre vai observar o proprio diretorio onde ele esta
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer() # instancia uma classe do observador do watchdog
    tp = TextParser() # instancia a classe do parser
    event_handler = DirEventHandler(tp, path) # cria o gerenciador de eventos
    # seta o observar para usar o gerenciador de eventos no diretorio
    observer.schedule(event_handler, path = path)
    observer.start()
    print(f'Iniciando a observção do diretório -> {path}')
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()