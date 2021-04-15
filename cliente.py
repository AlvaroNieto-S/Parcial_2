from flask import Flask, render_template, request,redirect, url_for, flash
import json 

app=Flask(__name__)

app.secret_key="mysecretkey"

@app.route('/cliente')
def Index():
    return render_template('crear.html')

@app.route('/creado', methods=['POST'])
def crear():
    if request.method=='POST':
        id=request.form['id']
        nombre=request.form['nombre']
        apellidos=request.form['apellidos']
        direccion=request.form['direccion']
        cod_postal=request.form['codigo']
        
        x={
                
                "id": int(id),
                "nombre": nombre,
                "apellidos":apellidos,
                "direccion":direccion,
                "cod_postal":int(cod_postal)
            
        }
        
        with open('cliente.json','w') as informacion:
            json.dump(x,informacion,indent=4 ,sort_keys=False)

        flash('Cliente creado exitosamente')
        return redirect(url_for('Index'))

@app.route('/cliente/<id>')
def mostrar(id):
    with open('cliente.json') as informacion:
        datos= json.loads(informacion.read())
    if int(id)==int(datos['id']):
        return datos
    else:
        return 'la id no existe :c'

@app.route('/cliente/actualizar/<a>')
def actualizar(a):
    with open('cliente.json') as informacion:
        datos= json.loads(informacion.read())
    if int(a)==int(datos['id']):
        return render_template('obtener.html')
    else:
        return 'La id no existe :c'        

@app.route('/actualizado', methods=['POST'])
def actualizado():
        if request.method=='POST':
            nombre=request.form['nombre']
            apellidos=request.form['apellidos']
            direccion=request.form['direccion']
            cod_postal=request.form['codigo']

            with open('cliente.json') as informacion:
                datos= json.loads(informacion.read())
                print(datos)
            id=datos['id']
            x={
                
                "id": int(id),
                "nombre": nombre,
                "apellidos":apellidos,
                "direccion":direccion,
                "cod_postal":int(cod_postal)
            
            }
            print(x)
            with open('cliente.json','w') as informacion:
                json.dump(x,informacion,indent=4)

            flash('Cliente actualizado exitosamente.')
            return redirect(url_for('actualizar',a=id))


if __name__== '__main__':
    app.run(port=3000, debug=True)