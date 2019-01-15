import unittest
import httpretty
import requests
import os
import json
from worker.worker import Client

directory = f'{os.path.dirname(os.path.realpath(__file__))}/videos'
class ClientClassTestCase(unittest.TestCase):

    @httpretty.activate
    def test_post_cut(self):
        client = Client('https://httpbin.org/post', 'https://httpbin.org/post', directory)
        content = { "to_cut": { "start_time": "16/12/2018 00:51:54;16", "end_time": "16/12/2018 01:38:24;0", "title": "SUP - (DES)ENCONTRO PERFEITO - S", "duration": "00:46:29;15", "reconcile_key": "20181215234" } }
        path = { "video_path": client.video_path }
        content.update(path)
        httpretty.enable()
        httpretty.register_uri( httpretty.POST,
                                "https://httpbin.org/post",
                                body=json.dumps(content)
                            )
        response = client.post_cut(json.dumps(content))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), content)
        httpretty.disable()
        httpretty.reset()   

    def test_get_cut(self):
        client = Client('http://httpbin.org/ip', 'http://api.globo_play', directory)
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, "http://httpbin.org/ip", body='{"origin": "127.0.0.1"}', status=202)
        response = client.get_cut(1)
        self.assertEqual(response.json(), {'origin': '127.0.0.1'})
        httpretty.disable()
        httpretty.reset() 