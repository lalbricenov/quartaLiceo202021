from flask import Flask, render_template, request, redirect

# Crear la aplicacion. __name__ representa el archivo actual
app = Flask(__name__)

# personas es una lista(array) de diccionarios
personas = [{"nombre":"Juan", "apellido":"Rodriguez"}, {"nombre":"Maria", "apellido":"Rodriguez"}]

# rutas disponibles
# / quiere decir root
@app.route('/')
def index():
    # return str(personas)
    return render_template('index.html', personas = personas)
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
        apellido = request.form.get('apellido')
        personaNueva  = {'nombre':nombre, 'apellido':apellido}
        personas.append(personaNueva)

        # return f'Se va  a añadir la persona {nombre} {apellido}'
        return redirect('/')
# esto permite acceder a rutas como /persona/4, /persona/2341234
@app.route('/persona/<int:persona_id>')
def persona(persona_id):
    return f'Aca se verán los detalles de la persona {persona_id}'

@app.route('/delete/<int:persona_id>')
def delete(persona_id):
    return f'Acá se borra la persona con id {persona_id}'

@app.route('/modify/<int:persona_id>')
def modify(persona_id):
    return f'Acá se modifican los datos de la persona con id {persona_id}'