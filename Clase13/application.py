from flask import Flask, render_template, request, redirect

## __name__ corresponde al nombre del archivo actual
app = Flask(__name__)

# Variable que almacenara las tareas
tareas = []

@app.route("/")
def tasks():
    return render_template("index.html", tareas = tareas)

# Por defecto la aplicación sólo responde al metodo de solicitud GET.
# Para que responda al método POST debemos especificarlo
@app.route('/add', methods = ['GET', 'POST'])
def add():
    # El usuario visita la ruta /add cuando quiere añadir una tarea
    # y luego de presionar el botón enviar
    if request.method == 'GET':
        # Si el usuario va a añadir una tarea
        return render_template("add.html")
    if request.method == 'POST':
        # Si el usuario presionó el botón enviar
        # Debemos añadir la tarea a la lista
        tareaNueva = request.form.get("tarea")
        tareas.append(tareaNueva)
        # Mostrar la lista de tareas
        return redirect('/')

