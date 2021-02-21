$( document ).ready(function() {
    $("#submitbutton").click(start_game);
});

function fade_in(t, id, key, final_line) {
  if(!final_line) {
    $('#output').append("<p id='" + id + "'></p>")  
  } else {
    $('#output').append("<p id='" + id + "' class='titles'></p>")  
  }
  $("#" + id).hide();
  $("#" + id).html(t['text'][key].join('</br>'));
  $("#" + id).fadeIn(1000);
}

function write_text(t) {
  var i;
  for (i = 1; i < Object.keys(t['text']).length; i++) {
    var id = "div" + i.toString();
    fade_in(t, id, i.toString(), false);
  }
  fade_in(t, 'result', 'result', true);
}

function start_game() {
  
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
    $.ajax({
        url: $SCRIPT_ROOT + "/game",
        type: 'post',
        dataType: 'json',
        data: data,
        success: function(data) {
          write_text(data);
        }
    });
  }
}