
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
    par = impar = 0
    mayor =  cnt = counter = 0
    j = 1
    aseDes = 1

    for i in range(maxIter) :
        if ( secuencia[i] == 1):
            break
        if ( secuencia[i] % 2 == 0):
            par = par + 1
            secuencia.append(secuencia[i] / 2)
            cnt = cnt + 1
        else:
            impar = impar + 1
            secuencia.append( ( secuencia[i] * 3 ) + 1 )
            cnt = cnt + 1
        
        anterior = secuencia[1]
        while (j != cnt):
            if ( aseDes == 1):
                if (secuencia[j] > anterior):
                    aseDes = 0
                    counter = counter + 1
                    mayor = counter if ( counter > mayor ) else mayor
            else :
                if ( secuencia[j] < anterior ):
                    aseDes = 1
                    counter = counter + 1
                    mayor = counter if ( counter > mayor ) else mayor
            j = j + 1
    
    print secuencia
    print "S = " + str(inicio)
    print "L = " + str(maxIter)
    print "Lof = " + str(cnt)
    print "P = " + str(par)
    print "I = " + str(impar)
    print "N = " + str(mayor / 2)
    

generarSecuencia()
