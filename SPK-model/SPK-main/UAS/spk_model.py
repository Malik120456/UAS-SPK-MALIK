from settings import MEREK_SCALE,DEV_SCALE_ram,DEV_SCALE_prosesor,DEV_SCALE_storage,DEV_SCALE_baterai,DEV_SCALE_harga,DEV_SCALE_ukuran_layar

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'brand': 5, 
            'ram': 3, 
            'prosesor': 4, 
            'storage': 3, 
            'baterai': 4, 
            'ukuran_layar': 3, 
            'harga': 1
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': smartphone['id'],
            'brand': MEREK_SCALE[smartphone['brand']],
            'ram': DEV_SCALE_ram[smartphone['ram']],
            'prosesor': DEV_SCALE_prosesor[smartphone['prosesor']],
            'storage': DEV_SCALE_storage[smartphone['storage']],
            'baterai': DEV_SCALE_baterai[smartphone['baterai']],
            'ukuran_layar': DEV_SCALE_ukuran_layar[smartphone['ukuran_layar']],
            'harga': DEV_SCALE_harga[smartphone['harga']]
        } for smartphone in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brand = [] # max
        ram = [] # max
        prosesor = [] # max
        storage = [] # max
        baterai = [] # max
        ukuran_layar = [] # max
        harga = [] # min
        for data in self.data:
            brand.append(data['brand'])
            ram.append(data['ram'])
            prosesor.append(data['prosesor'])
            storage.append(data['storage'])
            baterai.append(data['baterai'])
            ukuran_layar.append(data['ukuran_layar'])
            harga.append(data['harga'])

        max_brand = max(brand)
        max_ram = max(ram)
        max_prosesor = max(prosesor)
        max_storage = max(storage)
        max_baterai = max(baterai)
        max_ukuran_layar = max(ukuran_layar)
        min_harga = min(harga)

        return [
            {   'id': data['id'],
                'brand': data['brand']/max_brand, # benefit
                'ram': data['ram']/max_ram, # benefit
                'prosesor': data['prosesor']/max_prosesor, # benefit
                'storage': data['storage']/max_storage, # benefit
                'baterai': data['baterai']/max_baterai, # benefit
                'ukuran_layar': data['ukuran_layar']/max_ukuran_layar, # benefit
                'harga': min_harga/data['harga'] # cost
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['brand'] ** weight['brand'] *
        row['ram'] ** weight['ram'] *
        row['prosesor'] ** weight['prosesor'] *
        row['storage'] ** weight['storage'] *
        row['baterai'] ** weight['baterai'] *
        row['ukuran_layar'] ** (-weight['ukuran_layar']) *
        row['harga'] ** weight['harga']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))