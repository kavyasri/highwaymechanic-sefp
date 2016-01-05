$(document).ready(function(){
    window.ajax_url_mapper = {
        '/':'/location/confirm/',
        '/accounts/register/':'/accounts/register/',
        '/accounts/login/':'/accounts/login/'
    };
    window.redirect_mapper = {
       '/':'/location/confirm/',
    };
    window.urlname = window.location.pathname;
    
window.addr = '';
getLocation();



function getLocation() {
    if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else { 
        alert('Please share your location to avail our services');
    }
}

$('#mapholder').load(function(){
        $('.loading-gif').hide();
    });

function showPosition(position) {
    window.lat = position.coords.latitude;
    window.lon = position.coords.longitude;

     $.ajax({
        	method: 'GET',
        	url: window.ajax_url_mapper[window.urlname],
        	data: {	    lati : position.coords.latitude,
			    longi : position.coords.longitude,			
		},
        	success: function (data) {
             	
        	},
        	error: function (data) {
        	     alert("Your location seems to be unavailable at the moment. Please try again");
        	}
    });	    
}

function initialize() {
  var usercenter = new google.maps.LatLng(window.lat,window.lon);  
  var mapproperties = {
    center:usercenter,
    zoom:18,
    panControl:true,
    zoomControl:true,
    mapTypeControl:true,
    scaleControl:true,
    streetViewControl:true,
    overviewMapControl:true,
    rotateControl:true,    
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("mapholder"), mapproperties);
  var marker=new google.maps.Marker({
  position:usercenter,
  });

marker.setMap(map);
} 

google.maps.event.addDomListener(window, 'load', initialize);
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation."
            break;
        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable."
            break;
        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out."
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred."
            break;
    }
}
});

