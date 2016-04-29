 var buttons = document.getElementsByClassName("button-color");
for(var i=0;i<buttons.length;i++) {
  buttons[i].classList.add(i % 2 === 0 ? "even" : "odd");
  //or
  buttons[i].style["background-color"] = i % 2 === 0 ? "#FF6600" : "#696666";
}
