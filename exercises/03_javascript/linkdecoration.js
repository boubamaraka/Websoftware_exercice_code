// Exercise 2.3 Javascript file  //
// Read the instructions.html //

//some helpful debug code
// href="http://google.com"
$("#javascript_start").html("[OK] Started executing the javascript file");
$("#javascript_end").html("[WAITING]...this far we haven't reached the end... Maybe you should try FireBug?");

// ADD YOUR CODE BETWEEN THESE LINES //
/*$( document ).ready(function() {

  // $("a[href='.pdf']").addClass("pdf");
  //  $("a[href='.zip']").addClass("download ");
     //$("a[href='.xyz']").addClass("download ");

  $("a[href$='.pdf']").addClass("pdf")
//$("a[href$='.zip']").addClass("download")
  //  $("a[href$='.xyz']").addClass("download")
    //$("a:not([href$='.pdf,.html'])").addClass("download")
    $("a:not([href$='.pdf'])a:not([href$='.html'])").each(function(){

     var domain=$this;
     var sub=domain.attr("href").split(". ");
    if( sub[sup.index-1] >=0)
     $("a[domain]").addClass("download");



   });




});
*/
$( document ).ready(function() {

  // $("a[href='.pdf']").addClass("pdf");
  //  $("a[href='.zip']").addClass("download ");
     //$("a[href='.xyz']").addClass("download ");

  $("a[href$='.pdf']").addClass("pdf")
  $("a[href$='.zip']").addClass("download")
    $("a[href$='.xyz']").addClass("download")
      $("a[href$='.doc']").addClass("download")



});








// ADD YOUR CODE BETWEEN THESE LINES //

//some helpful debug code

$("#javascript_end").html("[OK] The end of your javascript file was reached. (meaning there were no huge errors) Hopefully your code works too! ");
