$(document).ready(function(){
    $.get("https://fourtonfish.com/hellosalut/?lang=fr?callback=?",
    function(data){
        console.log(data);
    },
    "json"
    );
});