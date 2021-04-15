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

####### Pakage #####

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

####### Factura #######

app3=Flask(__name__)
app3.secret_key="mysecretkey"

@app3.route('/factura')
def crearf():
    return render_template('factura.html')

@app3.route('/creando', methods=['POST'])
def creando():
    if request.method=='POST':
        id=request.form['id']
        cliente=request.form['cliente']
        paquete=request.form['paquete']
        fecha=request.form['fecha']

        with open('cliente.json') as informacion:
            datos=json.loads(informacion.read())
        
        with open('paquete.json') as informacion2:
            datos2=json.loads(informacion2.read())
        
        if int(cliente)==int(datos['id']) and int(paquete)==int(datos2['id']):
            total=int(datos2['costo'])
            x={
                
            "id": int(id),
            "total":total,
            "fecha":fecha,
            "cliente":datos,
            "paquete":[datos2['nombre']]
             }

            with open('factura.json','w') as informacion:
                json.dump(x,informacion,indent=4)

            return "factura creada"
        
        if int(cliente)!=int(datos['id']) and int(paquete)==int(datos2['id']):
            return "No existe el cliente"

        if int(cliente)==int(datos['id']) and int(paquete)!=int(datos2['id']):
            return "No existe el paquete"
        
        if int(cliente)!=int(datos['id']) and int(paquete)!=int(datos2['id']):
            return "No existe el cliente ni el paquete"

@app3.route('/factura/<idf>')
def mostrarf(idf):
    with open('factura.json') as informacion:
        datos= json.loads(informacion.read())
    if int(idf)==int(datos['id']):
        return render_template('mostrar.html', factura=datos)
    else:
        return 'la id no existe :c'
@app3.route('/agregar_paquete')
def agregarp():
    return render_template('crearp2.html')

@app3.route('/agregando', methods=['POST'])
def agregando():
    if request.method=='POST':
        ida=request.form['id']
        with open('paquete.json') as informacion2:
            datos2=json.loads(informacion2.read())
        if int(ida)==int(datos2['id']):
            with open('factura.json') as informacion:
                datos=json.loads(informacion.read())
            pa=datos['paquete']
            pa.append(datos2['nombre'])
            sumac=int(datos2['costo'])
            nuevo_total=sumac+int(datos['total'])
            idf=datos['id']
            fecha=datos['fecha']
            cliente=datos['cliente']
            
            x={
                
            "id": int(idf),
            "total":nuevo_total,
            "fecha":fecha,
            "cliente":cliente,
            "paquete": pa 
             }

            with open('factura.json','w') as informacion:
                json.dump(x,informacion,indent=4)
            flash('Paquete agregado exitosamente')
            return redirect(url_for('mostrarf',idf=idf))
        else:
            return "eso no existe"

@app3.route('/eliminar_paquete')
def eliminar_paquete():
    return render_template('eliminar.html')

@app3.route('/eliminando', methods=['POST'])
def eliminandof():
    if request.method=='POST':
        ida=request.form['id']
        with open('paquete.json') as informacion2:
            datos2=json.loads(informacion2.read())
        if int(ida)==int(datos2['id']):
            with open('factura.json') as informacion:
                datos=json.loads(informacion.read())
            pa=datos['paquete']
            pa.remove(datos2['nombre'])
            sumac=int(datos2['costo'])
            nuevo_total=int(datos['total'])-sumac
            idf=datos['id']
            fecha=datos['fecha']
            cliente=datos['cliente']
            
            x={
                
            "id": int(idf),
            "total":nuevo_total,
            "fecha":fecha,
            "cliente":cliente,
            "paquete": pa 
             }

            with open('factura.json','w') as informacion:
                json.dump(x,informacion,indent=4)
            flash('Paquete eliminado exitosamente')
            return redirect(url_for('mostrarf',idf=idf))
        else:
            return "eso no existe"

if __name__== '__main__':
    app.run(port=3000, debug=True)