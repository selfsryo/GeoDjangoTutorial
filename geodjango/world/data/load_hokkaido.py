import os

from django.contrib.gis.utils import LayerMapping

from world.models import Border


mapping = {
    'n03_001' : 'N03_001',
    'n03_002' : 'N03_002',
    'n03_003' : 'N03_003',
    'n03_004' : 'N03_004',
    'n03_007' : 'N03_007',
    'geom' : 'POLYGON',
}

geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hokkaido.geojson'))

def run(verbose=True):
    lm = LayerMapping(Border, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
