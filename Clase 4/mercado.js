let compras = ["Arroz", "Lentejas", "Papas"];
let lista = document.querySelector("#listaMercado");

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

let input = document.querySelector("#inputAdd");
let btn = document.querySelector("#btnAdd");

// Event listener
function addItem() {
  // leer el valor que el usuario escribio
  let item = input.value;
  compras.push(item);
  hacerLista();
  //Borrar lo que el usuario escribio
  input.value = "";
}
btn.onclick = addItem;
hacerLista();
