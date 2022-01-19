from django.conf.urls import url                                                                                                                              
from . import views
from django.urls import path


urlpatterns = [ 
    path('rast_val/<slug:lat>/<slug:lon>/', views.get_salt),
    path('city_val/<slug:city>/', views.get_city_coords),
    # path('pgmap/', views.show_map, name="folium_map"),
    path(r'map/', views.show_map_2, name="folium_map"),
    url(r'mapwms/', views.show_map_3, name="mapgeoserver"),
    path('tutorial', views.show_tutorial, name="folium_map"),
    path('', views.default_map, name="folium_map")
]