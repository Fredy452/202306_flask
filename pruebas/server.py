"""Importa Flask para permitirnos crear nuestra aplicación"""
from flask import Flask 


app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


"""El decorador "@" asocia esta ruta con la función inmediatamente siguiente"""
@app.route('/')
def hola_mundo():
    """Devuelve la cadena '¡Hola Mundo!' como respuesta"""
    return '<h1>Hello world</h1>'


"""Creamos otra ruta"""
@app.route('/inicio/')
def ruta_inicio():
    return '<h2>Esto es un inicio</h2>'


"""
Asegúrate de que este archivo se esté 
ejecutando directamente y no desde un módulo diferente
"""
if __name__== "__main__":
    """Ejecuta la aplicación en modo de depuración"""
    app.run(debug=True)

