from flask import Flask, render_template, request,redirect, url_for, flash
import json 

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
    app3.run(port=3002, debug=True)