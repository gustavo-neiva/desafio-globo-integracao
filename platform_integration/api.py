import json
import requests

r = requests.post('https://dff71640-01ba-4181-a65d-c7538dcb5bb4.mock.pstmn.io')

print(r)
class Api():
    pass

    #TODO
    #POST videos a serem cortados - api/v1/corte
    # - { "cuts" : [
        # { "start_time": "timecode",
        # "end_time": "timecode",
        # "path": "path arquivo a ser salvo" }
        #  ]
    # }
    # GET  status do corte e video api/v1/corte/:id a cada x tempo

    # POST para api g
