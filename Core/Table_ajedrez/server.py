from flask import Flask, render_template


app = Flask(__name__)


"""El decorador "@" asocia esta ruta con la función inmediatamente siguiente"""
@app.route('/')
def tablero():
    return render_template('index.html')


@app.route('/<int:numero>')
def tablero_dos(numero):
    print(numero)
    return render_template('number.html', numero=numero)


@app.route('/<int:x>/<int:y>/')
def tablero_x_y(x, y):
    print(x, y)
    return render_template('number2.html', vertical=x, horizontal=y)


@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>/')
def tablero_x_y_color(x, y, color1, color2):
    print(x, y, color1, color2)
    return render_template('color.html', vertical=x, horizontal=y, color1=color1, color2=color2)  # noqa: E501

if __name__== "__main__":
    """Ejecuta la aplicación en modo de depuración"""
    app.run(debug=True)