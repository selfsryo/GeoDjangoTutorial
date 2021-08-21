from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from world.models import Border, School, Facility, Busstop



class BorderAdmin(LeafletGeoAdmin):
    search_fields = ['n03_001','n03_003','n03_004']
    list_filter = ('n03_003')

admin.site.register(Border, LeafletGeoAdmin)
admin.site.register(School, LeafletGeoAdmin)
admin.site.register(Facility, LeafletGeoAdmin)
admin.site.register(Busstop, LeafletGeoAdmin)

admin.site.site_title  = 'GeoDjangoログイン'
admin.site.site_header = 'GeoDjangoハンズオン'
admin.site.index_title = 'GeoDjangoメニュー'
