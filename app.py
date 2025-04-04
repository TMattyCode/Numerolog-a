from flask import Flask, render_template, request
import numeros as n
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def mostrarResultado():
    nombre=request.form.get('nombre')
    resultado1=f'Numero de expresión: {n.numeroExpresion(nombre)}'
    resultado2=f'Numero de alma: {n.numeroAlma(nombre)}'
    return render_template('index.html',resultado1=resultado1,resultado2=resultado2)

def abrir_navegador():
    webbrowser.open_new('http://localhost:5000/')

def iniciar_app():
    threading.Timer(1, abrir_navegador).start()  # espera un segundo y abre
    app.run(use_reloader=False)

if __name__ == '__main__':
    iniciar_app()