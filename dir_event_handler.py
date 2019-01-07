from watchdog.events import FileSystemEventHandler

class DirEventHandler(FileSystemEventHandler):
    def process(self, event):
        pass
        
    def on_created(self, event): # quando o arquivo for criado no diretorio
        self.process(event)