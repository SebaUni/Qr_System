from xml.dom.minidom import Element
import QR_Codificacion as qrc
from PIL import Image
import os

def UpdateDelete():
    rut = input("Introduzca su rut: ")
    opcion = input("Si quieres eliminar usuario, presiona 1. Si quieres editar, presiona 2: ")
    if opcion == "1":
        os.remove('qrs/'+rut+'.png')
        print("Archivo eliminado")
    elif opcion == "2":
        os.remove('qrs/'+rut+'.png')
        nombre = input("Introduzca su nombre: ")
        apellido = input("Introduzca su apellido: ")
        rut = input("Introduzca su rut: ")
        cadena = rut + ";" + nombre + ";" + apellido
        imagen= qrc.qr.make(cadena)
        nombre_imagen = rut + ".png"
        archivo_imagen = open("qrs/"+nombre_imagen, 'wb')
        imagen.save(archivo_imagen)
        archivo_imagen.close()
    else:
        print("Opcion no valida")

def AgregarUsuario():
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")
    rut = input("Introduzca su rut: ")
    cadena = rut + ";" + nombre + ";" + apellido
    imagen= qrc.qr.make(cadena)
    nombre_imagen = rut + ".png"
    archivo_imagen = open("qrs/"+nombre_imagen, 'wb')
    imagen.save(archivo_imagen)
    archivo_imagen.close()
    ruta_imagen = 'qrs/' + nombre_imagen
    Image.open(ruta_imagen).show()

def DatosUsuario(ruta_qr):
    ruta_qr= "qrs/{}.PNG".format(ruta_qr)
    element= qrc.Descodificacion(ruta_qr)
    print("Descodificado ruta {0}:\nNombre:{1}\nApellido:{2}\nRut{3}\n",ruta_qr,element[1],element[2],element[0])

def CodificacionCSV(csv):
    file= open(csv,"r")
    flag = 0
    for x in file:
        element= x.split(",")
        if(flag != 0): 
            element[0]= element[0].strip()
            element[1]= element[1].strip()
            element[2]= element[2].strip()
            qrc.Codificacion(element[0],element[1],element[2])
        else:
            flag+=1