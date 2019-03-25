from set_config import setup
import urllib
import json


class GraphRequest:
    def __init__(self):
        settings = setup()

        # get url pieces
        self.frag_url = settings.get('fragalysis', 'url')
        self.graph_url = settings.get('graph', 'search')
        self.query = settings.get('graph', 'query')

        # get full url
        self.search_url = str(self.frag_url + self.graph_url + self.query)

        # set blanks for smiles search and json to handle later
        self.smiles_url = None
        self.graph_json = None

    def set_smiles_url(self, smiles):
        # set full search url
        self.smiles_url = str(self.search_url + smiles)

    def get_graph_json(self):
        # check for a smiles url
        if not self.smiles_url:
            raise Exception('Please initiate smiles url with set_smiles_url(<smiles>)!')

        # get response from url and decode -> json
        with urllib.request.urlopen(self.smiles_url) as f:
            response = json.loads(f.read().decode('utf-8'))

        # set json as decoded response for processing
        self.graph_json = response

        return response
