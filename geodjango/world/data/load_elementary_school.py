import os

from django.contrib.gis.utils import LayerMapping

from world.models import School


mapping = {
    'a27_001' : 'A27_001',
    'a27_002' : 'A27_002',
    'a27_003' : 'A27_003',
    'a27_004' : 'A27_004',
    'geom'    : 'POINT',
}

geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'elementary_school.geojson'))

def run(verbose=True):
    lm = LayerMapping(School, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
