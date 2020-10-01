let compras = ["Arroz", "Lentejas", "Papas"];
let lista = document.querySelector("#listaMercado");
let tabla = document.querySelector("#tablaTareas");

// Opcion 1, for como en C
// for (let i = 0; i < compras.length; i++) {
//   let elemento = document.createElement("li");
//   elemento.innerHTML = compras[i];
//   lista.appendChild(elemento);
// }

// Opcion 2, for of.
// Se hace lo mismo para cada uno de los elementos de la lista.
function hacerLista() {
  lista.innerHTML = "";
  for (item of compras) {
    let elemento = document.createElement("li");
    elemento.innerHTML = item;
    lista.appendChild(elemento);
  }
}

function addHeaders() {
  let fila = document.createElement("tr");
  let enc1 = document.createElement("th");
  enc1.innerHTML = "Materia";
  let enc2 = document.createElement("th");
  enc2.innerHTML = "Descripción";
  let enc3 = document.createElement("th");
  enc3.innerHTML = "Fecha";

  fila.appendChild(enc1);
  fila.appendChild(enc2);
  fila.appendChild(enc3);
  tabla.appendChild(fila);
}

function hacerTabla() {
  tabla.innerHTML = "";
  addHeaders();
  for (item of compras) {
    let fila = document.createElement("tr");
    // Creo los datos que van en la fila
    let tdMateria = document.createElement("td");
    tdMateria.innerHTML = item; //en su programa esto hara referencia al dato de materia ingresado por el usuario
    let tdDescripcion = document.createElement("td");
    tdDescripcion.innerHTML = item; //en su programa esto hara referencia al dato de descripcion ingresado por el usuario
    let tdFecha = document.createElement("td");
    tdFecha.innerHTML = item; ////en su programa esto hara referencia al dato de fecha ingresado por el usuario

    // Añado los nuevos datos como children de la fila
    fila.appendChild(tdMateria);
    fila.appendChild(tdDescripcion);
    fila.appendChild(tdFecha);

    // Añado la fila a la tabla
    tabla.appendChild(fila);
  }
}

let input = document.querySelector("#inputAdd");
let btn = document.querySelector("#btnAdd");

// Event listener
function addItem() {
  // leer el valor que el usuario escribio
  let item = input.value;
  compras.push(item);
  hacerLista();
  hacerTabla();
  //Borrar lo que el usuario escribio
  input.value = "";
}
btn.onclick = addItem;
hacerLista();
hacerTabla();
