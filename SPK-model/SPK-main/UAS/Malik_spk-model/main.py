import sys
from colorama import Fore, Style
from models import Base, Smartphone
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import DEV_SCALE_bran,DEV_SCALE_ram,DEV_SCALE_prosesor,DEV_SCALE_storage,DEV_SCALE_baterai,DEV_SCALE_harga,DEV_SCALE_ukuran_layar

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-5
        self.raw_weight = {'brand': 5, 'ram': 3, 'prosesor': 4, 'storage': 3, 'baterai': 4, 'ukuran_layar': 3, 'harga': 1}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k,v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphone)
        return [{'id': smartphonerealme.id, 
        'brand': DEV_SCALE_bran[smartphonerealme.brand], 
        'ram': DEV_SCALE_ram[smartphonerealme.ram], 
        'prosesor': DEV_SCALE_prosesor[smartphonerealme.prosesor], 
        'storage': DEV_SCALE_storage[smartphonerealme.storage], 
        'baterai': DEV_SCALE_baterai[smartphonerealme.baterai], 
        'ukuran_layar': DEV_SCALE_ukuran_layar[smartphonerealme.ukuran_layar], 
        'harga': DEV_SCALE_harga[smartphonerealme.harga]} for smartphonerealme in session.scalars(query)]
    
    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brands = [] # max
        rams = [] # max
        prosesors = [] # max
        storages = [] # max
        baterais = [] # max
        ukuran_layars = [] # max
        hargas = [] # min
        for data in self.data:
            brands.append(data['brand'])
            rams.append(data['ram'])
            prosesors.append(data['prosesor'])
            storages.append(data['storage'])
            baterais.append(data['baterai'])
            ukuran_layars.append(data['ukuran_layar'])
            hargas.append(data['harga'])
        max_brand = max(brands)
        max_ram = max(rams)
        max_prosesor = max(prosesors)
        max_storage = max(storages)
        max_baterai = max(baterais)
        max_ukuran_layar = max(ukuran_layars)
        min_harga = min(hargas)
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
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result =  {row['id']:
            round(
                row['brand']**weight['brand'] *
                row['ram']**weight['ram'] *
                row['prosesor']**weight['prosesor'] *
                row['storage']**weight['storage'] *
                row['baterai']**weight['baterai'] *
                row['ukuran_layar']**weight['ukuran_layar'] *
                row['harga']**weight['harga'],
            2)
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['id']:
            round(row['brand'] * weight['brand'] +
            row['ram'] * weight['ram'] +
            row['prosesor'] * weight['prosesor'] +
            row['storage'] * weight['storage'] +
            row['baterai'] * weight['baterai'] +
            row['ukuran_layar'] * weight['ukuran_layar'] +
            row['harga'] * weight['harga'], 2)
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)
    

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)
    pass

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
