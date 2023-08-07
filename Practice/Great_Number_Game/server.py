from flask import Flask, render_template, request, session, redirect

# import the random module
import random

app = Flask(__name__)

# Creamos secret key para session 
app.secret_key = "supersecret"


@app.route('/')
def localhost():
    """
    Ruta de inicio
    """
    # random number between 1-100
    number = random.randint(1, 100)
    session['randon'] = number
    session['count'] = 0

    return render_template('dashboard.html', randon=session['randon'])  # noqa: E501


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Ruta de inicio
    """
    print(f"El numero randon es: {session['randon']}")
    print(f"El numero enviado es: {request.form['number']}")

    result = ''
    if session['randon'] == int(request.form['number']):
        result = 'Adivinaste'
        print(result)
    elif session['randon'] > int(request.form['number']):
        result = 'Es menor'
        session['count'] += 1
        print(result)
    elif session['randon'] < int(request.form['number']):
        result = 'Es Mayor'
        session['count'] += 1
        print(result)

    return render_template('dashboard.html', result=result, count=session['count'])  # noqa: E501


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    """
    Restablece los valores y redirige a la página principal
    """
    session['randon'] = random.randint(1, 100)
    session['intentos'] = 0
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)