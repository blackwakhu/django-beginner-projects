function deletedata(){
  window.alert("you are deleting the piece of data");
}

function open_data(btn, input){
  let mybtn = document.getElementById(btn)
  let myinput = document.getElementById(input)
  myinput.style.display = "block"
  mybtn.style.display = "none"
}

function close_data(btn, input){
  let mybtn = document.getElementById(btn)
  let myinput = document.getElementById(input)
  myinput.style.display = "none"
  mybtn.style.display = "block"
}
