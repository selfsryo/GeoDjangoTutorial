import os

from django.contrib.gis.utils import LayerMapping

from world.models import Busstop


mapping = {
    'p11_001' : 'P11_001' ,
    'p11_002' : 'P11_002',
    'p11_003_1' : 'P11_003_1',
    'p11_003_2' : 'P11_003_2',
    'p11_003_3' : 'P11_003_3',
    'p11_003_4' : 'P11_003_4',
    'p11_003_5' : 'P11_003_5',
    'p11_003_6' : 'P11_003_6',
    'p11_003_7' : 'P11_003_7',
    'p11_003_8' : 'P11_003_8',
    'p11_003_9' : 'P11_003_9',
    'p11_003_10' : 'P11_003_10',
    'p11_003_11' : 'P11_003_11',
    'p11_003_12' : 'P11_003_12',
    'p11_003_13' : 'P11_003_13',
    'p11_003_14' : 'P11_003_14',
    'p11_003_15' : 'P11_003_15',
    'p11_003_16' : 'P11_003_16',
    'p11_003_17' : 'P11_003_17',
    'p11_003_18' : 'P11_003_18',
    'p11_003_19' : 'P11_003_19',
    'p11_004_1' : 'P11_004_1',
    'p11_004_2' : 'P11_004_2',
    'p11_004_3' : 'P11_004_3',
    'p11_004_4' : 'P11_004_4',
    'p11_004_5' : 'P11_004_5',
    'p11_004_6' : 'P11_004_6',
    'p11_004_7' : 'P11_004_7',
    'p11_004_8' : 'P11_004_8',
    'p11_004_9' : 'P11_004_9',
    'p11_004_10' : 'P11_004_10',
    'p11_004_11' : 'P11_004_11',
    'p11_004_12' : 'P11_004_12',
    'p11_004_13' : 'P11_004_13',
    'p11_004_14' : 'P11_004_14',
    'p11_004_15' : 'P11_004_15',
    'p11_004_16' : 'P11_004_16',
    'p11_004_17' : 'P11_004_17',
    'p11_004_18' : 'P11_004_18',
    'p11_004_19' : 'P11_004_19',
    'geom'    : 'POINT',
}

geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'busstop.geojson'))

def run(verbose=True):
    lm = LayerMapping(Busstop, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
