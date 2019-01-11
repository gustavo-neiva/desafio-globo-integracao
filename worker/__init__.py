from .client import Client

cut_url = 'https://jsonplaceholder.typicode.com/posts' # api de exemplo para testes
globo_play_url = 'https://jsonplaceholder.typicode.com/posts'
video_path = "path/to/save/video"
client = Client(cut_url, globo_play_url, video_path) # instancia a class do http client