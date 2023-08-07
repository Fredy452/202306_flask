# Impotamos flask
from flask import Flask, render_template, request, session


# Creamos una instancia 
app = Flask(__name__)

# Creamos secret key para session 
app.secret_key = "supersecret"


# Ruta de inicio
@app.route('/')
def inicio():
    """Ruta de inicio"""

    # Cramos contador de sessiones
    if 'count' in session:
        print('la llave existe!')
        session['count'] += 1
    else:
        session['count'] = 1

    return render_template('contador.html', count=session['count'])


# Creamos la ruta destroy session
@app.route('/destroy_session/', methods=['POST'])
def destroy_session():
    """
    Ruta para borrar session
    """
    session.clear()
    session['count'] = 1
    return render_template('contador.html', count=session['count'])


# Creamos la ruta add visit
@app.route('/add_visit/', methods=['POST'])
def add_visit():
    """
    Funcion para incrementar las visitas por 2
    """
    if 'count' not in session:
        """Verificamos si el contador esta vacio"""
        session['count'] = 1

    session['count'] += 2
    return render_template('contador.html', count=session['count'])


# Creamos ruta para input
@app.route('/manual_increment', methods=['POST'])
def manual_increment():
    """
    Funcion que recive el numero de visitas
    """
    print(request.form['numero'])
    if 'count' not in session:
        """Verificamos si el contador esta vacio"""
        session['count'] = 1

    session['count'] += int(request.form['numero'])
    return render_template('contador.html', count=session['count'])
    


# Creamos el punto de arranque
if __name__=="__main__":
    app.run(debug=True)