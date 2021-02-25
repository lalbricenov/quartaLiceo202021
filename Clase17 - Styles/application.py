from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app) # indica que quiero usar sesiones en la aplicacion app

# tareas = []
@app.route("/")
def index():# se define una función
    if "tareas" not in session:
        session['tareas'] = []
    return render_template('index.html', tareas = session['tareas'])
    # session['tareas'] # Esto me dice las tareas de este usuario


@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'GET':
        # Mostrarle al usuario el fomulario
        return render_template('add.html')
    else:
        nombre = request.form.get('nombre')
        if nombre == None or nombre == '':
            print('Hubo un error')
            mensaje = {"contenido":"La tarea no puede ser vacía", "tipo":"error"}
            return render_template('add.html', mensaje = mensaje)

        print(f'La tarea ingresada fue: {nombre}')
        session['tareas'].append(nombre)
        mensaje = {"contenido":"Nueva tarea añadida exitosamente", "tipo":"exito"}
        return render_template('index.html', tareas = session['tareas'], mensaje=mensaje)






