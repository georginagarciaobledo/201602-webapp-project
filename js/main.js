 var buttons = document.getElementsByClassName("button-color");
for(var i=0;i<buttons.length;i++) {
  buttons[i].classList.add(i % 2 === 0 ? "even" : "odd");
  //or
  buttons[i].style["background-color"] = i % 2 === 0 ? "#FF6600" : "#696666";
}

function alternate(id){

  if(document.getElementsByTagName){

    var table = document.getElementById(id);

    var rows = table.getElementsByTagName("tr");

    for(i = 0; i < rows.length; i++){

  //manipulate rows

      if(i % 2 == 0){

        rows[i].className = "even";
        .even{background-color: gray;};

      }else{

        rows[i].className = "odd";

      }

    }

  }

}
