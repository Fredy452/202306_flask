#Importando flask
from flask import Flask, render_template


# Creando instancia de la clase flask
app = Flask(__name__)


# A continuación se van a definir las rutas
@app.route('/')
def create_html():
    """Creamos la ruta donde vamos aredirigir a nuestro table.html"""

    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


    return render_template('table.html', users=users)








# Creando punto de arranque
if __name__ == "__main__":
    """Ejecutando la aplicaciónen modo depuración"""
    app.run(debug=True)