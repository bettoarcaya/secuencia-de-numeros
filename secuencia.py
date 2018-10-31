
def leerDatos():
    file = open("archivo.txt", "r")
    datos = file.read()
    arr = datos.split(" ")
    return arr

def generarSecuencia():
    data = leerDatos()
    inicio = int(data[0])
    maxIter = int(data[1])
    secuencia = []
    secuencia.append(inicio)
    i = 0

    for i in range(maxIter) :
        if ( secuencia[i] == 1):
            break
        if ( secuencia[i] % 2 == 0):
            secuencia.append(secuencia[i] / 2)
        else:
            secuencia.append( ( secuencia[i] * 3 ) + 1 )
        i = i + 1

    print secuencia

generarSecuencia()
