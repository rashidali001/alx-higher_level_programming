$(document).ready(function(){
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json",
    function(data, textstatus){
        let arr = data.results;
        for( let i = 0; i < arr.length; i++){
            $("#list_movies").append("<li>"+arr[i].title+"</li>");
        }
    }
    );
});
