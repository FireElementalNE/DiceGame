$( document ).ready(function() {
    console.log( "ready!" );
    $("#submitbutton").click(start_game);
    var a;
});

function write_text(t) {
  // $('#output').html(data['text'].join('</br>'));
  console.log(Object.keys(t['text']).length);
  console.log(t['text']);
  var i, j;
  for (i = 1; i < Object.keys(t['text']).length; i++) {
    var id = "div" + i.toString();
    console.log(t['text'][i.toString()]);
    $('#output').append("<p id='" + id + "'></p>")
    $("#" + id).hide();
    // for(j = 0; j < t['text'][i.toString()].length; j++) {
    $("#" + id).html(t['text'][i.toString()].join('</br>'));
    $("#" + id).fadeIn(1000);
    // }

  }
}
function start_game() {
  var x, text;
  n1 = $("#name1").val();
  n2 = $("#name2").val();
  rounds = $("#rounds").val();
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
          write_text(data);
        }
    });
  }
}