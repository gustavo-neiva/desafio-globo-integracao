import unittest
import httpretty
import requests
import os
import json
from worker.client import Client

directory = f'{os.path.dirname(os.path.realpath(__file__))}/videos'
class ClientClassTestCase(unittest.TestCase):
    @httpretty.activate

    def test_post_cut(self):
        client = Client('https://httpbin.org/post', 'https://httpbin.org', directory)
        content = { "to_cut": { "start_time": "16/12/2018 00:51:54;16", "end_time": "16/12/2018 01:38:24;0", "title": "SUP - (DES)ENCONTRO PERFEITO - S", "duration": "00:46:29;15", "reconcile_key": "20181215234" } }
        path = { "video_path": client.video_path }
        content.update(path)
        httpretty.register_uri( httpretty.POST,
                                "https://httpbin.org/post",
                                body=json.dumps(content)
                            )
        response = client.post_cut(content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), content)
    # def test_get_cut(self):
    #     client = Client('https://httpbin.org/', 'http://api.globo_play', directory)
    #     httpretty.register_uri( httpretty.GET,
    #                             "https://httpbin.org/ip/1",
    #                             body='{"origin": "127.0.0.1"}'
    #                         )
    #     response = client.get_cut(1)
    #     response.should.equal({'origin': '127.0.0.1'})
    #     httpretty.latest_requests().should.have.length_of(1)
    #     httpretty.last_request().should.equal(httpretty.latest_requests()[0])
    #     httpretty.last_request().body.should.equal('{"origin": "127.0.0.1"}')

    

    # def test_post_globo_play(self, mock_get):
    #     pass