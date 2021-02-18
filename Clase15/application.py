from flask import Flask, render_template, request, redirect
from cs50 import SQL

db = SQL("sqlite:///evento.db")

# Crear la aplicacion. __name__ representa el archivo actual
app = Flask(__name__)


# rutas disponibles
# / quiere decir root
@app.route('/')
def index():
    asistentes = db.execute("SELECT * FROM asistentes")
    # print(asistentes[0]["email"])
    return render_template("index.html", asistentes = asistentes)

# El usuario va a acceder a la ruta /add con el método get cuando escriba
# en la url /add.
# El usuario va a acceder a la ruta /add con el método post cuando haga
# click en enviar el formulario, luego de llenar los datos de la nueva persona
@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        # return 'Aca se muestra el formulario para llenar los datos'
        return render_template('add.html')
    else:
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        edad = request.form.get('edad')
        # añadir la persona a la base de datos
        db.execute(f"INSERT INTO asistentes ('nombre', 'email', 'edad') VALUES (:name, :email, :edad)", name=nombre, email=email, edad=edad)
        # return f'Se va  a añadir la persona {nombre} {apellido}'
        return redirect('/')
# esto permite acceder a rutas como /persona/4, /persona/2341234
@app.route('/persona/<int:persona_id>')
def persona(persona_id):
    # deben escribir el comando para obtener de la base de datos la persona
    # que tiene el id persona_id
    asistentes = db.execute('SELECT * FROM asistentes where....')
    # len(asistentes)==0
    return f'Acá se verán los detalles de la persona {persona_id}'

@app.route('/delete/<int:persona_id>')
def delete(persona_id):
    # deben escribir el comando para borrar de la base de datos la persona
    # que tiene el id persona_id

    # Supongamos que noté que no existe la persona que se quiere borrar
    # Mostrar una página con un mensaje de error
    # Por ejemplo supongamos que el usuario 20 no existe
    if persona_id == 20:
        return render_template('error.html', mensaje = f"La persona con el id {persona_id} no existe")
    return f'Acá se borra la persona con id {persona_id}'

@app.route('/modify/<int:persona_id>')
def modify(persona_id):
    return f'Acá se modifican los datos de la persona con id {persona_id}'