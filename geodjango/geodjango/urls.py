from django.contrib.gis import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter

from world.views import BorderViewSet, SchoolViewSet, FacilityViewSet, BusstopViewSet, GeojsonAPIView, index


router = DefaultRouter()
router.register('border', BorderViewSet)
router.register('school', SchoolViewSet)
router.register('facility', FacilityViewSet)
router.register('busstop', BusstopViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='world_index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('world/geojson/', GeojsonAPIView.as_view(), name='geojson_view'),
]