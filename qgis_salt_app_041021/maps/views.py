from django.shortcuts import render
from branca.element import Element, JavascriptLink
import folium
from folium.raster_layers import ImageOverlay
from js_functions import get_geo, navbarhtml, latlng_zoom, latlng_beta, load_images
# import branca.colormap as cm
from django.db import connection
from django.http import JsonResponse
import os

# this function works to get the the land type classification from a certain location
def get_salt(request, lat='', lon=''):
    try:
        latitude = float(lon.replace('x','.'))
        longitude = float(lat.replace('x','.'))
        'http://127.0.0.1:8000/salt/rast_val/-75x52698/39x10226/'
        """-75.52698,39.10226"""
        """QUERY FROM DATABASE"""
        with connection.cursor() as cursor:
            raw_query = f"SELECT ST_Value(rast, ST_SetSRID(ST_MakePoint({latitude},{longitude}),4326)) AS 
            val FROM Kent_2017 WHERE ST_Intersects(rast, ST_SetSRID(ST_MakePoint({latitude},{longitude}),4326));"
            # print(raw_query)
            cursor.execute(raw_query)
            for val in cursor.fetchall():
                salt_val_17 = val
                break
        print(salt_val_17)
        with connection.cursor() as cursor:
            raw_query = f"SELECT ST_Value(rast, ST_SetSRID(ST_MakePoint({latitude},{longitude}),4326)) AS 
            val FROM Kent_2013 WHERE ST_Intersects(rast, ST_SetSRID(ST_MakePoint({latitude},{longitude}),4326));"
            # print(raw_query)
            cursor.execute(raw_query)
            for val in cursor.fetchall():
                salt_val_13 = val
                break
        print(salt_val_13)
        return JsonResponse({'Value17': f'{salt_val_17[0]}', 'Value13': f'{salt_val_13[0]}', 'Lat':f'{latitude}','Long':f'{longitude}','Exception':'No'})
    except Exception as E:
        print(E)
        return JsonResponse({'Value17': '', 'Value13': '', 'Lat':f'{latitude}','Long':f'{longitude}','Exception':'Yes'})


#used to show map with the layers of raster files 
def show_map(request):
    #creation of map comes here + business logic
    m = folium.Map([39.0874, -75.6189], height=800, zoom_start=8)
    m.add_child(folium.LatLngPopup_Beta())
    # m.add_child(folium.LatLngPopup())


    map_id = m.get_name()
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('Stamen Water Color').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)


    """ADDING OR REMOVING IMAGES WITH BOUNDS"""
    img_2017 = ImageOverlay(
        name="Kent_2017",
        image=fr'{os.getcwd()}/media/Kent2017.png',
        bounds=[[38.450723828315, -75.789989154039], [39.839519282115, -75.048879031539]],
        zindex=1,
        opacity=1
    )

    folium.Popup("Kent 2017").add_to(img_2017)
    img_2017.add_to(m)
    img_2013 = ImageOverlay(
        name="Kent_2013",
        image=fr'{os.getcwd()}/media/Kent2013.png',
        bounds=[[38.450723828315, -75.789989154039], [39.839519282115, -75.048879031539]],
        zindex=1,
        opacity=1
    )
    folium.Popup("Kent 2013").add_to(img_2013)
    img_2013.add_to(m)


    folium.LayerControl().add_to(m)

    # m.get_root().script.add_child(Element(latlng_beta % {'map_id':map_id, 'ken13':img_2013.get_name(), 'ken17':img_2017.get_name()}))
    m.get_root().script.add_child(Element(latlng_zoom % {'map_id':map_id, 'ken13':img_2013.get_name(), 'ken17':img_2017.get_name()}))
    m.get_root().html.add_child(Element(navbarhtml))
    m.get_root().script.add_child(Element(get_geo % {'map_id':map_id}))
    m.get_root().script.add_child(Element(load_images % {'map_id':map_id, 'ken13':img_2013.get_name(), 'ken17':img_2017.get_name()}))
    

    m=m._repr_html_() #updated
    context = {'my_map': m}

    return render(request, 'map_pg.html', context)


def get_city_coords(request, city):
    try:
        with connection.cursor() as cursor:
            raw_query = "SELECT ST_X(geom), ST_Y(geom) from world_cities where city_name = '{}';".format(city)
            print(raw_query)
            cursor.execute(raw_query)
            for val in cursor.fetchall():
                salt_val_17 = val
                print('SALT: ', salt_val_17)
        return JsonResponse({'Lat': f'{salt_val_17[0]}', 'Lon': f'{salt_val_17[1]}'})
    except Exception as E:
        return JsonResponse({'Lat': '', 'Lon': ''})


def default_map(request):
    return render(request, 'default.html', {})

def show_map_2(request):
    return render(request, 'map_geo.html', {})

    
def show_tutorial(request):
    return render(request, 'tutorial.html', {})

def show_map_3(request):
    return render(request, 'map_wms.html', {})