async function  obtenerLanzamientos(){
    var accessToken = "a0fc6ade9e744beeb9375fb12e66d6b8";

$.ajax({
    url: 'https://api.spotify.com/v1/browse/new-releases',
    type: 'GET',
    headers: {
        'Authorization' : 'Bearer ' + a0fc6ade9e744beeb9375fb12e66d6b8
    },
    success: function(data) {
        console.log(data);
        // Handle the response data here
    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.error('Error:', errorThrown);
        // Handle error
    }
});
}


