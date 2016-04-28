var buttons = document.getElementsByClassName("buttons-color");
for(var i=0;i<buttons.length;i++) {
  buttons[i].classList.add(i % 2 === 0 ? "even" : "odd");
  //or
  buttons[i].style["background-color"] = i % 2 === 0 ? "#f15b22" : "#696666";
}