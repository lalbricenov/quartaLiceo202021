// variables
//  dynamic typing language
let x = 4;
let nombre = "Luis";
let y = 2.5;
let estudiar = true;

// operadores
console.log(x + 3);
// concatenar cadenas de caracteres
console.log(nombre + " Briceño");
console.log(!estudiar || (false && true));

// backtick strings
console.log(`La suma de x + 3 es: ${x + 3}`);
console.log(`El valor e y es ${y}, y al sumarle la x obtengo: ${x + y}`);

if (x > y) {
  console.log("x es mayor que y");
} else {
  if (x == y) {
    console.log("x es igual a y");
  } else {
    console.log("x es menor a y");
  }
}
