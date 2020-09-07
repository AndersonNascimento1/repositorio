#!python
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        print('Download completo')
        for cidade in csv.reader(entrada.read().decode('latin1').splitlines()):
            if cidade[0] == 'FID':
                continue
            print('{8} : {3}'.format(*cidade))


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
