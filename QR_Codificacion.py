import qrcode as qr

def Codificacion(Nombre, Apellido, rut):
    print("Codificando {}\n".format(rut))
    data= "{0};{1};{2}".format(rut,Nombre,Apellido)
    img = qr.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save("./qrs/{0}.png".format(rut))

def Descodificacion(img):
    q= qr.Decoder(img)
    element= q.split(";")
    element[0]= element[0].strip()
    element[1]= element[1].strip()
    element[2]= element[2].strip()
    return element