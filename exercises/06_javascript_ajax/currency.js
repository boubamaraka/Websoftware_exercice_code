$(document).ready(function(){
  $("#form").submit(function(e){
    data=document.getElementById('date').value;
    console.log(data);
    e.preventDefault();
    dateUrl="http://api.fixer.io/"+data;
 var myurl = dateUrl + encodeURIComponent(dateUrl);
// var me=document.getElementById("date").value;
 //console.log(myurl);
 //console.log(dateUrl);
 //jQuery.getJSON(myurl, function(data) { console.log(data.rates); });

 $.ajax({
    url: myurl,
    jsonp: "callback",
    dataType: "jsonp",

    success: function( response ) {
        //console.log( response ); // server response
          $('#currencies').empty();
        $.each(response.rates, function(i, item) {
             var tr = document.createElement('tr');
             var td1 = document.createElement('TD');
             var td2 = document.createElement('TD');
              td1.appendChild(document.createTextNode(i));
              td2.appendChild(document.createTextNode(item));
              tr.appendChild(td1);
              tr.appendChild(td2);

              $('#currencies').append(tr);
              $('TD').css("border","1px solid #000");

          });

    }
});
 /*$("#form").submit(function(e){
   e.preventDefault();
    jQuery.getJSON(myurl,null, function(data) { $.each(data.rates, function(i, item) {
         var tr = document.createElement('tr');
         var td1 = document.createElement('TD');
         var td2 = document.createElement('TD');
          td1.appendChild(document.createTextNode(i));
          td2.appendChild(document.createTextNode(item));
          tr.appendChild(td1);
          tr.appendChild(td2);

          $('#currencies').append(tr);
          $('TD').css("border","1px solid #000");

      });




});
});*/
});
});
