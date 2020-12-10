# import sirve para incluir un módulo de python, libreria.
from flask import Flask, render_template
import random
## __name__ corresponde al nombre del archivo actual
app = Flask(__name__)

# ruta /. Cada vez que el usuario pida esa ruta vamos a ejecutar la función
# que está justo debajo
@app.route("/")
def index():
    # index es un nombre que yo escojo, le pongo index porque es la ruta base.
    return "Hello world"

@app.route("/goodbye")
def goodbye():
    return "<h1> Goodbye </h1> <p>Hola quarta liceo, y chao quarta liceo</p>"

@app.route("/lanzar")
def lanzar():
    # generar numero aleatorio
    number = random.randint(1, 2)
    # con render_template se genera el archivo html a partir de la
    # plantilla y de los valores de las variables en python
    return render_template("lanzar.html", numero=number)

listaEstudiantes = [{"nombre":"Antonio", "nota":7.8},{"nombre":"Maria", "nota":7.6}, {"nombre":"Pedro", "nota":6.5}]

@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html", estudiantes=listaEstudiantes)
