// nombres: string
// apellidos: string
// edad: int
// curso: string
// notas: array de floats
let estudiantes = [
  {
    nombres: "Pedro Antonio",
    apellidos: "Perez Rodriguez",
    edad: 45,
    curso: "Seconda",
    notas: [6.7, 9.4, 7.3, 4.5, 6.8],
  },
  {
    nombres: "Juan Antonio",
    apellidos: "Gomez Perez",
    edad: 54,
    curso: "Prima",
    notas: [6.5, 7.4, 8.3, 5.5, 7.8],
  },
  {
    nombres: "Marcos Juan",
    apellidos: "Gonzalez Duarte",
    edad: 6,
    curso: "Quarta",
    notas: [5.8, 8.3, 9.3, 6.5, 9.8],
  },
];

let tabla = document.querySelector("#tablaEstudiantes");
for (estudiante of estudiantes) {
  let fila = document.createElement("tr");
  for (valor of Object.values(estudiante)) {
    let celdaNueva = document.createElement("td");
    celdaNueva.innerHTML = valor;
    fila.appendChild(celdaNueva);
  }
  tabla.appendChild(fila);
}
