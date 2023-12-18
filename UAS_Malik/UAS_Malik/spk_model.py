from settings import WARMINDO_SCALE,DEV_SCALE_Harga_Minuman,DEV_SCALE_Harga_Makanan,DEV_SCALE_tahun_berdiri,DEV_SCALE_jumlah_menu,DEV_SCALE_kode

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'Warkop': 5, 
            'Harga_Minuman': 3, 
            'Harga_Makanan': 4, 
            'tahun_berdiri': 3, 
            'jumlah_menu': 4, 
            'kode': 3, 
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
            'Harga_Minuman': DEV_SCALE_Harga_Minuman[warmindo['Harga_Minuman']],
            'Harga_Makanan': DEV_SCALE_Harga_Makanan[warmindo['Harga_Makanan']],
            'tahun_berdiri': DEV_SCALE_tahun_berdiri[warmindo['tahun_berdiri']],
            'jumlah_menu': DEV_SCALE_jumlah_menu[warmindo['jumlah_menu']],
            'kode': DEV_SCALE_kode[warmindo['kode']],
        } for warmindo in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        Warkop = [] # max
        Harga_Minuman = [] # min
        Harga_Makanan = [] # min
        tahun_berdiri = [] # max
        jumlah_menu = [] # max
        kode = [] # max
        for data in self.data:
            Warkop.append(data['Warkop'])
            Harga_Minuman.append(data['Harga_Minuman'])
            Harga_Makanan.append(data['Harga_Makanan'])
            tahun_berdiri.append(data['tahun_berdiri'])
            jumlah_menu.append(data['jumlah_menu'])
            kode.append(data['kode'])

        max_Warkop = max(Warkop)
        max_Harga_Minuman = max(Harga_Minuman)
        max_Harga_Makanan = max(Harga_Makanan)
        max_tahun_berdiri = max(tahun_berdiri)
        max_jumlah_menu = max(jumlah_menu)
        min_kode = min(kode)

        return [
            {   'id': data['id'],
                'Warkop': data['Warkop']/max_Warkop, # benefit
                'Harga_Minuman': data['Harga_Minuman']/max_Harga_Minuman, # cost
                'Harga_Makanan': data['Harga_Makanan']/max_Harga_Makanan, # cost
                'tahun_berdiri': data['tahun_berdiri']/max_tahun_berdiri, # benefit
                'jumlah_menu': data['jumlah_menu']/max_jumlah_menu, # benefit
                'kode': min_kode/data['kode'] # benefit
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
        row['Harga_Minuman'] ** weight['Harga_Minuman'] *
        row['Harga_Makanan'] ** weight['Harga_Makanan'] *
        row['tahun_berdiri'] ** weight['tahun_berdiri'] *
        row['jumlah_menu'] ** weight['jumlah_menu'] *
        row['kode'] ** weight['kode']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))