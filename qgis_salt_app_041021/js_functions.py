load_images = """
    function load17(){
      %(map_id)s.removeLayer(%(ken13)s);
      %(ken17)s.addTo(%(map_id)s);
      var latlng = %(ken17)s.getBounds().getCenter();
      %(map_id)s.flyTo(latlng);  
      }
   function load13(){
      %(map_id)s.removeLayer(%(ken17)s);
      %(ken13)s.addTo(%(map_id)s);
      var latlng = %(ken13)s.getBounds().getCenter();
      
      %(map_id)s.flyTo(latlng);  
   }
      

"""

latlng_zoom = """
function set_popup_content(responseData){
  console.log(responseData);
  var display_content = "Latitude: " + lat +
    "<br>Longitude: " + lon;

    console.log(responseData);
  if (%(map_id)s.hasLayer(%(ken17)s) == true){
     display_content = display_content + "<br>Kent-2017: "+  landuse_type[~~responseData['Value17']-1];
  }
  if (%(map_id)s.hasLayer(%(ken13)s) == true){
     display_content = display_content +     "<br>Kent-2013: "+  landuse_type[~~responseData['Value13']-1];
  }
 return display_content;
}
    


function zoom2latlong(){
  const coordinates = document.getElementsByName("srch-term")[0].value.replace(" ", "");
  const myArr = coordinates.split(",");
  
  lat = myArr[0];
  lon = myArr[1];
  var latlng = L.latLng(myArr[0],myArr[1]);
  
  %(map_id)s.flyTo(latlng);  
  var query_url = '';
  var this_name = L.popup();
  query_url = query_url.concat('/rast_val/', lat.replace(".", "x"),'/',lon.replace(".", "x"),'/');
  console.log(query_url);            
  sendHttpRequest('GET', query_url).then(responseData => {
  this_name.setLatLng(latlng);
  
  var display_content = "Latitude: " + lat +
    "<br>Longitude: " + lon;

    console.log(responseData);
  if (%(map_id)s.hasLayer(%(ken17)s) == true){
     display_content = display_content + "<br>Kent-2017: "+  landuse_type[~~responseData['Value17']-1];
  }
  if (%(map_id)s.hasLayer(%(ken13)s) == true){
     display_content = display_content +     "<br>Kent-2013: "+  landuse_type[~~responseData['Value13']-1];
  }

  console.log(display_content);
  this_name.setContent(
    display_content
    ).openOn(%(map_id)s);});
}
"""

navbarhtml = """
<header style="position: fixed;">
  <div class="header">
      <div class="container">
          <div class="logo">
              <img src="https://stpubsecdev.blob.core.windows.net/webappassets/qgis/images/logo/logo-udel1.png">
          </div>
          <div class="nav">
              <ul>
                  <li><a href="/">Home</a></li>
                  <li><a href="pgmap">Map</a></li>
                  <li><a href="tutorial">Tutorial</a></li>
                  <li><a href="/">Publications</a></li>
              </ul>
          </div>
      </div> 
  </div>        
</header>
<nav class="navbar navbar-inverse" style="margin-bottom:0px">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"></a>
    </div>
    <div  class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
              <li class="active"><a href="#">Home</a></li>
              <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#">Layer
              <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><button type="button" class="btn btn-danger navbar-btn" value="2017" onclick=load17()>Kent 2017</button></li>
                <li><button type="button" class="btn btn-warning navbar-btn" value="2013" onclick=load13()>Kent 2013</button></li>
              </ul>
            </li>
          </ul>
          <button type="button" class="btn btn-dark navbar-btn"  onclick=getLocation()>
            <span class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>
          </button>
              <form class="navbar-form navbar-right">
            <div class="form-group">
              <input type="text" placeholder="Latitude,Longitude" name="srch-term"  id="srch-term" class="form-control" placeholder="Search">
            </div>
            <button type="button" class="btn btn-default" onclick=zoom2latlong()><i class="glyphicon glyphicon-search"></i></button>
          </form>
        
      </div>
    </div>
    </nav>
"""

get_geo = """

function getLocation() {
  if (navigator.geolocation) {
    console.log("You have clicked on live location");
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
    console.log(position);
    var latlng = L.latLng(position.coords.latitude, position.coords.longitude);
    %(map_id)s.flyTo(latlng);

    var query_url = '';
    var this_name = L.popup();
    query_url = query_url.concat('/rast_val/', position.coords.latitude.toString().replace(".", "x"),'/',position.coords.longitude.toString().replace(".", "x"),'/');
    console.log(query_url);            
    sendHttpRequest('GET', query_url).then(responseData => {
    this_name.setLatLng(latlng);

 
  var display_content = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;

    display_content = display_content + "<br>Kent-2017:  "+  landuse_type[responseData['Value17']-1];
    display_content = display_content + "<br>Kent-2013: "+  landuse_type[responseData['Value13']-1];

    this_name.setContent(
      display_content
      ).openOn(%(map_id)s);});
}"""

latlng_beta = """
const landuse_type = ["Forest", "Marsh", "Salt Water Intrusion", "Built",
    "Open Water", "Crop Fields", "Bare Soil Areas", "Open Field"];
const sendHttpRequest = (method, url, data) => {
    return fetch(url, {
    method: method,
    body: JSON.stringify(data),
    headers: data ? { 'Content-Type': 'application/json' } : {}
    }).then(response => {
    if (response.status >= 400) {
      // !response.ok
      return response.json().then(errResData => {
        const error = new Error('Something went wrong!');
        error.data = errResData;
        throw error;
      });
    }
    return response.json();
    });
    }

    var popup = L.popup();
    
    const getData = (e) => {
            var query_url = '';
            var value = 0;
            lon = e.latlng.lat.toFixed(4);
            lat = e.latlng.lng.toFixed(4);
            query_url = query_url.concat('/rast_val/', lat.replace(".", "x"),'/',lon.replace(".", "x"),'/');     
                   
            sendHttpRequest('GET', query_url).then(responseData => {
            popup.setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                "<br>Longitude: " + e.latlng.lng.toFixed(4)+
                "<br>Kent-2017: "+  landuse_type[~~responseData['Value17']-1]+
                "<br>Kent-2013: "+  landuse_type[~~responseData['Value13']-1]
                ).openOn(%(map_id)s);
            });}
    
    function latLngget(e) {
      console.log(e);
    popup.setLatLng(e.latlng);         
    getData(e);
    }
    %(map_id)s.on('click', latLngget);
    
"""

