function display_map(latitude, longitude) {
    var latlng = new google.maps.LatLng(latitude, longitude);
    var opts = {
        zoom: 14,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map"), opts);
    var m_latlng;
    var marker;
    m_latlng = new google.maps.LatLng(latitude, longitude);
    marker = new google.maps.Marker({
        position: m_latlng,
        map: map
    });
}
