
/* -------- Toggles the "Open filter" div -------*/
$(".search-filter").hide();
$("#more-filters").click(function(){
    $(".search-filter").slideToggle();
})

/* ---------- Copy link to clipboard ------------ */
/* ---------- Credits to W3 schools https://www.w3schools.com/howto/howto_js_copy_clipboard.asp -----------*/
/*---- Changed for my project ----------*/
function copyURL() {
  var copyText = document.getElementById("advert-url");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
}

/* ---------------------- Toggles Most viewed advert and most recent adverts -------------- */
$("#carousel-top-ad").hide();
$("#carousel-recent").hide();

$("#most-viewed").click(function (){
    $("#carousel-top-ad").slideToggle();
})

$("#most-recent").click(function (){
    $("#carousel-recent").slideToggle();
})