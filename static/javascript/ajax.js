$(document).ready(function(){
  $("#numofticks").change(function(){
    value = $("#numofticks").value();
    tic = '{{ ticketprice }}';
    ticket = int(tic);
    total = value * ticket;
    $("#totalprice").html(total);
  });
  // $("#btnsubmit").click(function(event){
  //   event.preventDefault();
  //   var formdata = $("#ticketsform").serialize();
  //
  //   $.ajax({
  //     url: "/",
  //     data: formdata,
  //     type: 'POST',
  //     success: function(response){
  //       console.log(response);
  //     },
  //     error: function(error){
  //       console.log(error);
  //     }
  //   });

  // });
});
