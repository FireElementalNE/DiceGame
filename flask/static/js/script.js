$( document ).ready(function() {
    console.log( "ready!" );
    $("#submitbutton").click(start_game);
    var a;
});

function start_game() {
  var x, text;

  // Get the value of the input field with id="numb"
  n1 = $("#name1").val();
  n2 = $("#name2").val();
  rounds = $("#rounds").val();

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(rounds) || n1 == "" || n2 == "") {
    console.log("Invalid Input");
  } else {
    $("#info_submission").hide();
    $("#names").html(n1 + " vs. " + n2 + " for " + rounds + " rounds. </br></br>");
    $("#gamespace").show();
    var data = {"n1": n1, "n2": n2, "rounds": rounds};
    console.log(data);
    $.ajax({
        url: $SCRIPT_ROOT + "/hello",
        type: 'post',
        dataType: 'json',
        data: data,
        success: function(data) {
            $('#output').html(data['text'].join('</br>'));
                   // ... do something with the data...
                 }
    });
  }
}