"""Importa Flask para permitirnos crear nuestra aplicación"""
from flask import Flask, render_template


app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


#Mostrando boxes
@app.route('/play/<int:number>/<string:color>')
def ruta_dojo(number, color):
    if number == '':
        number = 0
    print(number)
    print(color)
    return render_template('index.html', number=number, color=color)



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

