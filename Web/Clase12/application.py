# import sirve para incluir un módulo de python, libreria.
from flask import Flask, render_template, request
import random # va a importar todo lo que esté en la libreria random
import datetime
import pytz
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
    print('El usuario quiere ver los estudiantes')
    return render_template("estudiantes.html", estudiantes=listaEstudiantes)

@app.route("/add")
def addNota():

    # debemos revisar que los datos sean válidos
    # server side validation
    datosValidos = True
    nota = request.args.get("nota")
    nombre = request.args.get("nombre")
    if nombre != None and nombre != '':
        print('El nombre ingresado es valido')
    else:
        datosValidos = False
    if nota != None:
        nota = float(nota) # convertir la cadena de caractes en un numero
        if nota >= 0 and nota <= 10:
            print('La nota ingresada es valida')
        else:
            datosValidos = False
    else:
        datosValidos = False

    # print(f'El nombre recibido fue: {nombre}, y la nota fue {nota}')
    if datosValidos:
        return render_template("formulario.html", nombre=nombre, nota=nota)
    else:
        return '<h1> DATOS INVALIDOS </h1>'

@app.route('/hora')
def hora():
    current_timeBog = datetime.datetime.now(pytz.timezone('America/Bogota'))
    current_timeRom = datetime.datetime.now(pytz.timezone('Europe/Rome'))
    return render_template('hora.html', horaBogota = current_timeBog, horaRoma =current_timeRom )