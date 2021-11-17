import json

class Encoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('TempoArea__'): v for k, v in vars(o).items()}