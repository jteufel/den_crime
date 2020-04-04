var state = 1;
var n_button_bool = false;
var c_button_bool = false;

var n_button_selected = "";
var c_button_selected = "";

var n_input= "";
var c_input= "";

var loaded = false;
var data = {};

var map_images = {"n_one":"bghighlight-1","n_two":"bghighlight-2","n_three":"bghighlight-3","n_four":"bghighlight-4", "n_five":"bghighlight-5"}


function change_n_Selection(btn) {
    var n_button = document.getElementById(btn);
    var image = document.getElementById("image");
      if (n_button_bool == false) {
          n_button.style.backgroundColor = "#0066ff"
          n_button_bool = true;
          n_button_selected = n_button
          image.classList.remove("bgimg-2");
          //image.classList.add("bgimg-3");

      }
      else {

          n_button_selected.style.backgroundColor = "#eee"
          n_button.style.backgroundColor = "#0066ff"
          image.classList.remove(map_images[n_button_selected.id])
          n_button_selected = n_button

        }


      image.classList.add(map_images[btn]);
   }

function change_c_Selection(btn) {

    var c_button = document.getElementById(btn);
        if (c_button_bool == false) {
            c_button.style.backgroundColor = "#0099ff"
            c_button_bool = true;
            c_button_selected = c_button
         }
        else {

            c_button_selected.style.backgroundColor = "#99d6ff"
            c_button.style.backgroundColor = "#0099ff"
            c_button_selected = c_button

           }
      }

function color_buttons_on_hover() {

    var button = document.getElementById("n_one");
    button.addEventListener("mouseover", hover_color(button));
    //button.addEventListener("mouseout", change_hover_color(button));

    function hover_color(btn){

        var but = document.getElementById(btn.id);
        but.style.backgroundColor = "#b3ffff";

    }

    function change_hover_color(btn){

        var but = document.getElementById(btn.id);
        but.style.backgroundColor = "#eee";

    }

  }


function return_data() {

  if (n_button_bool == true && c_button_bool == true){

      var neighboorhood_input = ""
      var crime_input = ""

      var neighboorhood_data = data[n_input]
      var crime_data = neighboorhood_data[c_input]

      var num_crimes = crime_data.length

      if (num_crimes == 0){

        to_write = "No Crimes Reported"

      }else{

        var to_write = ""

        for (var i = 0; i <num_crimes; i++) {

          to_write +=  "<br>"+crime_data[i]+"</br>"

          }
        }

      show_chart()
      document.getElementById('display_text').innerHTML = to_write

  }else{

      show_chart()
      document.getElementById('display_text').innerHTML = "SELECT BOTH A NEIGHBOORHOOD AND CRIME"

  }



}



function show_chart() {

  document.getElementById('chart').style.opacity = "0.7";
  document.getElementById('chart_x').style.opacity = "0.7";fgfg

}

function close_chart() {

  document.getElementById('display_text').innerHTML = "CHECK FOR MORE CRIMES";
  document.getElementById('chart_x').style.opacity = "0.0";

}

function set_n_input(input_string) {

  n_input = input_string;

}

function set_c_input(input_string) {

  c_input= input_string;

}

function assign(input) {

  if (loaded == false){

     //data = input;
     data = JSON.parse(input);
     loaded = true;
  }

}
