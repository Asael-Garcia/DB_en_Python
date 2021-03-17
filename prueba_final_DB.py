#prueba final de database con clases
import sqlite3
conexion=sqlite3.connect('Tercera_DB.db')#creo la base de datos y le asigno un nombre
cursor=conexion.cursor()#creo un cursor que me servira para indicar que hacer y donde haerlo


class CRUD:#metodo CRUD para la DV
    def __init__(self):
        #CREO LA TABLA QUE VOY A USAR PARA IR RELLENANDO TODO
        cursor.execute("CREATE TABLE IF NOT EXISTS PERSONAS(NOMBRE TEXT, APELLIDO TEXT, EDAD TEXT, LOCALIDAD TEXT)")
        #CREATE
    def rellenarTabla(self,nombre,apellido,edad,localidad):#metodo para rellenar la tabla, entran parametros
        cursor.execute("INSERT INTO PERSONAS (nombre,apellido,edad,localidad) VALUES (?,?,?,?)",(nombre,apellido,edad,localidad))#llamo al cursor
        #y le digo que ejecute el comando de insertar en la tabla personas en las columnas con los valores (values) desconocidos ya que van a entrar variables
        #despues cierro mi comando por decirlo asi, y paso las variables con las que se ve a rellenar
        conexion.commit()#actulizo los cambios en mi DB
        #UPDATE
    def actualziar(self,actualizacion,nombre):#para la actulizacion de datos
        #cursor.execute("UPDATE PERSONAS SET APELLIDO=? WHERE NOMBRE=? ",(actualizacion,nombre))
        sql='''UPDATE PERSONAS SET APELLIDO = ? WHERE NOMBRE=? '''#hago una variable que me servira para la actulizacion de datos
        #el formato es: UPDATE (tabla) SET (columna_con_valor_a_cambiar) = ? WHERE (valor_que_se_usa_de_referencia)=?
        #los signos de interrogacion son para que acepte variables
        args=(actualizacion,nombre)#otra variable que guarda los paramatros que entran en el metodo
        cursor.execute(sql,args)
        conexion.commit()#ejecuto el comando
        #READ
    def mostrarDB(self):
        cursor.execute("SELECT * FROM PERSONAS")#ejecuto el comando donde selecciono todo
        data=cursor.fetchall()#es para obtener todos los datos
        for row in data:#los separa en posiciones como los arrays
            print(row)#los imprimo
        #DELEATE
    def eliminarDatos(self,nombre):#paso como parametro el nombre de la persona a eliminar
        cursor.execute("DELETE FROM PERSONAS WHERE NOMBRE = ? ",(nombre,))#por pedos de algunas versiones de sqlite le tengo que poner la coma al final de la variable que se paso como parametro
        #para que de esta forma no de error
        #el formato del delate es de: ("DELETE FROM (tabla) WHERE (condicion)=?",(variable,))
        #actualizo la database
        conexion.commit()
    def cerrarDB(self):#esto sirve para cerar la DB
        cursor.close()#cierro mi cursor
        conexion.close()#cierro la database



class Persona:#clase persona que usara para crear Personas e ir almacenandolas en la DB, con sus gets y sus sets
    def __init__(self):
        self._nombre=""
        self._apellido=""
        self._edad=""
        self._localidad=""
    
    def setNombreApellido(self,nombre, apellido):
        self._nombre=nombre
        self._apellido=apellido
    
    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido

    def setEdad(self,edad):
        self._edad=edad

    def getEdad(self):
        return self._edad

    def setLocalidad(self,localidad):
        self._localidad=localidad

    def getLocalidad(self):
        return self._localidad

print("SISTEMA DE AÑADIDOD DE PERSONAS A UNA DATABASE")
#creacion de instacioas y variables que me serviran
continuar="s"
persona=Persona()
crud=CRUD()
menu=["INGRESAR PERSONA","Actualizar","Mostrar DB","Eliminar por nombre","SALIR"]
contador=0
while continuar=="s":#while para que se repita todo
    #muestro el menu
    nombre=""
    for i in range(len(menu)):
        print(str(i+1)+" "+ menu[i])
    seleccion=int(input("Selecciona una de las opciones del menu: "))#pido que elija una opcion
    #switch case dependiendo de la eleccion
    if seleccion==1:#opcion uno para que entre gente
        nombre=input("Dame le nombre de la persona: ")#pido nombre
        apellido=input("Dame el apellido de "+nombre+": ")#pido apellido
        persona.setNombreApellido(nombre,apellido)#los almacenos en mi objeto persona
        edad=input("Dame la edad que tiene: ")#pido la edad
        localidad=input("Localidad de donde vive: ")#pido la localdiad
        print("----------------\nIngresando a la DB")#mensaje que indica que esta ingresando a la DB
        try:#pongo en un try catch el metodo del objeto crud, llamo al metodo para rellenar la tabla y paso los parametros de arriba
            crud.rellenarTabla(nombre,apellido,edad,localidad)
            print("Registrado correctamente")#si tiene exito en rellenarlos manda este mensaje
        except:#de lo contrario
            print("Error")#manda error
        
        
    elif seleccion==2:#para actualizar datos
        nombre=input("Dame el nombre de la perciona a la que le actulizaras el apellido: ")#pido el nombre de la persona a la que se le va a actualizar el apellido
        apellido=input("Actualizacion de apellido: ")#actualizacion de apellido
        try:#en un try catch que intente actualizarlo
            crud.actualziar(apellido,nombre)
            print("Actualizacion exitosa")#aqui dice que lo logro
        except: #si da error manda este mensaje
            print("Error vuelva a rellenar el formulario")
        #para mostrar lo datos de la DB en consola
    elif seleccion==3:
        try:
            crud.mostrarDB()
        except:#por si da error por alguna cosa
            print("Error")

    elif seleccion==4:#para eliminar alguna fila por nombre
        nombre=input("Dame el nombre de la persona a borrar: ")#nombre de la persona a eliminar
        try:#intenta eliminarlo
            crud.eliminarDatos(nombre)
            print("Eliminacion exitosa")#si pudo manda este mensaje
        except:#sino pudo manda error
            print("Error")
    elif seleccion==5:#segunda opcion para salir
        crud.cerrarDB()#cierro la database
        #mando mensajes de salida
        print("Perfecto nos vemos")
        print("Data base cerrada")
        continuar="n"
    else:#no sea pendejo elija una de las opciones disponibles
        print("Selecciona una de las opciones disponibles")
