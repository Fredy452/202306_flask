"""Importa Flask para permitirnos crear nuestra aplicación"""
from flask import Flask


app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


"""El decorador "@" asocia esta ruta con la función inmediatamente siguiente"""
@app.route('/')
def hola_mundo():
    """Devuelve la cadena '¡Hola Mundo!' como respuesta"""
    return '<h1>¡Hola Mndo!</h1>'


"""Creamos otra ruta para Dojo"""
@app.route('/dojo/')
def ruta_dojo():
    return '<h2>Dojo</h2>'


@app.route('/soy/<string:name>')
def say_name(name):
    """Funcion say var_name"""
    return (f"<h1> ¡Hola, {name}!</h1>")


@app.route('/repeact/<int:n>/<string:name>')
def repeact(n, name):
    """Funcion que va a repitir los datos de acuerdo a los parameros recibidos"""
    if name != str:
        pass
    return (f"{name} \n" * n)


#manejo de rutas no encontradas
@app.errorhandler(404)
def ruta_no_encontrada(error):
    return "<h1>pagina no encontrada</h1>", 404


"""
Asegúrate de que este archivo se esté 
ejecutando directamente y no desde un módulo diferente
"""
if __name__== "__main__":
    """Ejecuta la aplicación en modo de depuración"""
    app.run(debug=True)

