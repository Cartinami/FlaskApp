$(document).ready(function(){

  $("#btnsubmit").click(function(){
    var formdata = $("#infoform").serialize();

    $.ajax({
      url: "/name",
      data: formdata,
      type: 'POST',
      success: function(response){
        console.log(response);
      },
      error: function(error){
        console.log(error);
      }
    });

  });
});
