encabezado = document.querySelector("h1");
console.log(encabezado);
texto = prompt("Ingrese el texto que quiere en el encabezado");
// innerHTML es el texto que esta dentro del elemento
encabezado.innerHTML = texto;

// backgroundColor corresponde al color del fondo
color = prompt("Ingrese el color deseado");
encabezado.style.backgroundColor = color;
body = document.querySelector("body");
body.style.backgroundColor = color;
