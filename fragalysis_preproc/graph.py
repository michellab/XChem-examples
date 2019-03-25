import configparser
import os
import urllib
import json


class GraphRequest:
    def __init__(self):
        # use config parser to get settings from config.ini
        settings_file = os.path.join(os.getcwd(),'fragalysis_preproc/config.ini')
        settings = configparser.ConfigParser()
        settings._interpolation = configparser.ExtendedInterpolation()
        settings.read(settings_file)

        # get url pieces
        self.frag_url = settings.get('fragalysis', 'url')
        self.graph_url = settings.get('fragalysis', 'graph_search')
        self.query = settings.get('fragalysis', 'query')

        # get full url
        self.search_url = str(self.frag_url + self.graph_url + self.query)

        self.smiles_url = None

    def set_smiles_url(self, smiles):
        # set full search url
        self.smiles_url = str(self.search_url + smiles)

    def get_graph_json(self):
        # check for a smiles url
        if not self.smiles_url:
            raise Exception('Please initiate smiles url with get_smiles_url(<smiles>)!')

        # get response from url and decode -> json
        with urllib.request.urlopen(self.smiles_url) as f:
            response = json.loads(f.read().decode('utf-8'))

        return response
