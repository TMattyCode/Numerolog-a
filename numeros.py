# Numero de expresión

diccionario={
    1:["A","J","S"],
    2:["B","K","T"],
    3:["C","L","U"],
    4:["D","M","V"],
    5:["E","N","W"],
    6:["F","O","X"],
    7:["G","P","Y"],
    8:["H","Q","Z"],
    9:["I","R","0"],
}

def letra_a_numero(nombre):
    suma=0
    for letra in nombre.upper():
        for numeroD,letrasD in diccionario.items():
            for letraD in letrasD:
                if letra==letraD:
                    suma=suma+numeroD
    return numerosMaestros(suma)

def letra_a_numero_vocales(nombre):
    suma=0
    for letra in nombre.upper():
        for numeroD,letrasD in diccionario.items():
            for letraD in letrasD:
                if letraD=="A" or letraD=="E" or letraD=="I" or letraD=="O" or letraD=="U":
                    if letra==letraD:
                        suma=suma+numeroD
    return numerosMaestros(suma)

def numeroExpresion(nombreCompleto):
    nombres=nombreCompleto.split(" ")
    suma=0
    for nombre in nombres:
        suma=suma+letra_a_numero(nombre)
    return numerosMaestros(suma)

def numeroAlma(nombreCompleto):
    nombres=nombreCompleto.split(" ")
    suma=0
    for nombre in nombres:
        suma=suma+letra_a_numero_vocales(nombre)
    return numerosMaestros(suma)

def numerosMaestros(suma):
    suma2=0
    suma3=0
    if suma==11 or suma==22 or suma==33:
        suma3=suma
    else:
        for numero in str(suma):
            suma2=suma2+int(numero)
    if suma2==11 or suma2==22 or suma2==33:
        suma3=suma2
    else:
        for numero in str(suma2):
            suma3=suma3+int(numero)
    return suma3