// EVENT LISTENERS
boton = document.querySelector("#boton1");
parraf = document.querySelector("#miParrafo");
function cambiarcolor() {
  parraf.style.backgroundColor = "red";
  alert("Color cambiado");
}
// Al hacer click sobre el boton queremos que se ejecute la funcion cambiarcolor
boton.onclick = cambiarcolor;
