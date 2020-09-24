//Variables
let x = 4;
let y = 3;
// Backtick string
console.log(`x + y = ${x + y}`);
console.log(`x - y = ${x - y}`);
console.log(`x * y = ${x * y}`);
console.log(`x / y = ${x / y}`);
console.log(`x % y = ${x % y}`);

// Condicionales y bucles
let w;
do {
  w = parseFloat(prompt("Ingrese un número"));
} while (Number.isNaN(w) || w < 0);
let nombre;
do {
  nombre = prompt("ingrese su nombre");
} while (nombre.length < 2);

// parseFloat convierte una cadena de caracteres en un numero decimal
// NaN: not a number
if (w > 0) {
  console.log(`${w} es positivo`);
} else {
  if (w < 0) console.log(`${w} es negativo`);
  else console.log(`${w} es cero`);
}

let nombre = "Sarah";
console.log(`La longitud del nombre es ${nombre.length}`);
