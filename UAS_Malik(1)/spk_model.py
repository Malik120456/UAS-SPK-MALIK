from settings import WARMINDO_SCALE,DEV_SCALE_kode,DEV_SCALE_tahun,DEV_SCALE_menu,DEV_SCALE_Harga

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'Warkop': 5, 
            'kode': 3,   
            'tahun': 3, 
            'menu': 4, 
            'Harga': 3
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
            'id': warmindo['id'],
            'Warkop': WARMINDO_SCALE[warmindo['Warkop']],
            'kode': DEV_SCALE_kode[warmindo['kode']],
            'tahun': DEV_SCALE_tahun[warmindo['tahun']],
            'menu': DEV_SCALE_menu[warmindo['menu']],
            'Harga': DEV_SCALE_Harga[warmindo['Harga']],
        } for warmindo in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        Warkop = [] # max
        kode = [] # max
        tahun = [] # max
        menu = [] # max
        Harga = [] # min

        for data in self.data:
            Warkop.append(data['Warkop'])
            kode.append(data['kode'])
            tahun.append(data['tahun'])
            menu.append(data['menu'])
            Harga.append(data['Harga'])

        max_Warkop = max(Warkop)
        max_kode = max(kode)
        max_tahun = max(tahun)
        max_menu = max(menu)
        min_harga = min(Harga)
        return [
            {   'id': data['id'],
                'Warkop': data['Warkop']/max_Warkop, # benefit
                'kode': data['kode']/max_kode, # benefit
                'tahun': data['tahun']/max_tahun, # benefit
                'menu': data['menu']/max_menu, # benefit
                'Harga': min_harga/data['Harga'] # benefit
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
        row['Warkop'] ** weight['Warkop'] *
        row['kode'] ** weight['kode'] *
        row['tahun'] ** weight['tahun'] *
        row['menu'] ** weight['menu'] *
        row['Harga'] ** weight['Harga']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))