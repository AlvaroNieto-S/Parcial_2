from flask import Flask, render_template, request,redirect, url_for, flash
import json 

app2=Flask(__name__)
app2.secret_key="mysecretkey"
@app2.route('/paquete')
def inicio():
    return render_template('crearp.html')

@app2.route('/trayectoria', methods=['POST'])
def calcular():
    if request.method=='POST':
        idp=request.form['id']
        origen=request.form['origen']
        destino=request.form['destino']
         
        if destino=='Local' or destino=='local':
            costo=3500
        if destino=='Centro America' or destino=='centro america':
            costo=5000
        if destino=='Norte America' or destino=='Norte America':
            costo=7500
        if destino=='Sur America' or destino=='Sur America':
            costo=7200
        if destino=='Europa' or destino=='europa':
            costo=12000
        if destino=='Asia' or destino=='asia':
            costo=13500
        if destino== 'Africa' or destino=='Africa':
            costo=11350

        x={   
            "id": int(idp),
            "origen": origen,
            "destino": destino,
            "costo": costo
            
        }
        print(x)
        with open('trayectoria.json','w') as informacion:
            json.dump(x,informacion,indent=4)

        return render_template('paque.html')
    
@app2.route('/crearpaquete', methods=['POST'])
def guardar():
    if request.method=='POST':
        idp=request.form['id']
        nombre=request.form['nombre']
        with open('trayectoria.json') as informacion:
            datos=json.loads(informacion.read())
            costo=datos['costo']
        x={
                
            "id": idp,
            "nombre": nombre,
            "costo": costo
        }
        print(x)
        with open('paquete.json','w') as informacion:
            json.dump(x,informacion,indent=4)

        flash('El paquete ha sido creado de manera satisfactoria.')
        return redirect(url_for('inicio'))

@app2.route('/paquete/<idp>')
def enseñar(idp):
    with open('paquete.json') as informacion:
        datos= json.loads(informacion.read())
    if int(idp)==int(datos['id']):
        return datos
    else:
        return 'la id no existe :c'

if __name__== '__main__':
    app2.run(port=3001, debug=True)