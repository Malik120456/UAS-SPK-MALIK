import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Warmindo():

    def __init__(self) -> None:
        self.warmindo = pd.read_csv('data/warkopi.csv')
        self.warmindos = np.array(self.warmindo)

    @property
    def warmindo_data(self):
        data = []
        for warmindo in self.warmindos:
            data.append({'id': warmindo[0], 'nama': warmindo[1]})
        return data

    @property
    def warmindo_data_dict(self):
        data = {}
        for warmindo in self.warmindos:
            data[warmindo[0]] = warmindo[1] 
        return data

    def get_recs(self, kriteria:dict):
        wp = WeightedProduct(self.warmindo.to_dict(orient="records"), kriteria)
        return wp.calculate

