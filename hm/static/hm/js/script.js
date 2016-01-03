$(document).ready(function(){
window.addr = '';
getLocation();

function redirecter(){
	window.location.href="/location/confirm/";
}

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
    lat = position.coords.latitude;
    lon = position.coords.longitude;
     $.ajax({
        	method: 'GET',
        	url: '/location/confirm',
        	data: {	    lati : position.coords.latitude,
			    long : position.coords.longitude,			
		},
        	success: function (data) {
             	
        	},
        	error: function (data) {
        	     alert("Your location seems to be unavailable at the moment. Please try again");
        	}
    });	    
	
    latlon = new google.maps.LatLng(lat, lon);
    geocoder = new google.maps.Geocoder();
    geocoder.geocode({'latLng':latlon},function(results,status){
        if(status == google.maps.GeocoderStatus.OK){
            window.addr = results[0].formatted_address;

        }
    });
    mapholder = document.getElementById('mapholder')
    mapholder.style.height = '70vh';
    mapholder.style.width = '100%';

    var myOptions = {
    center:latlon,zoom:14,
    mapTypeId:google.maps.MapTypeId.ROADMAP,
    mapTypeControl:false,
    navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
    }
    
    var map = new google.maps.Map(document.getElementById("mapholder"), myOptions);
    
    var marker = new google.maps.Marker({position:latlon,map:map,title:"you are here!"});
    console.log(addr);
}
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

