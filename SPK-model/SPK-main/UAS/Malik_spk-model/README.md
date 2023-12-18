
# spk_model

  

## Virtualenv

install, create, activate virtual environment using virtualenv

https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Install depedencies
run `pip install -r requirements.txt`

  

## create postgresql database

create database in your locals

modify settings.py 
  

## create table

run:

    python main.py create_table

  

## create data

run this query in your db client

    INSERT INTO public.house (developer,lb,lt,price) VALUES
    
    ('ciputra',75,80,850),
    
    ('sinarmas',70,50,950),
    
    ('sasmita',78,82,650),
    
    ('lippo',65,50,700),
    
    ('ciputra',65,70,750),
    
    ('sinarmas',120,110,1500);


## run SAW

     python main.py saw

https://github.com/agungperdananto/spk_model

## Tugas UAS 1
isi function berikut dengan metode WP
https://github.com/agungperdananto/spk_model/blob/78e8fea9ef5b7910ac1a3a819d7f3a2af5933043/main.py#L77-L80

contoh(metode SAW) dapat dilihat di 
https://github.com/agungperdananto/spk_model/blob/78e8fea9ef5b7910ac1a3a819d7f3a2af5933043/main.py#L85-L96

lalu implementasikan di data kalian masing-masing