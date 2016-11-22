$("#diceform").submit(function(event){
  event.preventDefault();
  // var isnumber = $.isnumeric($("#numofdice"));
  var quantity = $("#numofdice");

  $("#dicecontainer").html(quantity);

});
