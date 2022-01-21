from flask import Flask


app=Flask(__name__)
#RUTA 1
@app.route( '/' )
def hola():
    return "<h1>Hola Mundo</h1>"
#RUTA2
@app.route('/dojo')
def dojo():
    return "<h1>!Dojo!</h1>"

@app.route('/say/<string:name>')
def say(name):
    return "<h1>Hola," + name + "!</h1>"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    arr=""
    for i in range(0,num):
        arr = arr +"<h1>"+ name+"<br>"+"</h1>"
    return arr 
@app.errorhandler(404)
def ExceptionPersonalize(error):
    return "<h1>¡Lo siento! Pagina no encontrada. Intentalo otra vez!!!!.</h1>",404

if __name__=="__main__":
    app.run(debug=True)

