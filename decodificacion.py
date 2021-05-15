from random import randrange
import os


matrizDecodificada = [253, 254, 254, 255, 253, 253, 253, 255, 253, 254]
dic = {"e" : "011" , "c" : "000" , "d" : "01"}
def diffNull (num, decod, dic):
    keys = dic.keys()
    for k in keys:
        if num == dic[k]:
            decod.append(k)
    num = ""
    return num
#img = imagen a decodificar
#dic = diccionario
#name = nombre del txt
#   nombre del txt = Decrypt + name 
def decodHuff(img, dic,name):
    a = img[:,:,3]
    print("asdasdasda",a)
    matrizDecodificada= a.flatten() #Vector unidimencional
    #LLena los primeros pixeles de la componente a
    print(matrizDecodificada)
    num = ""
    decod = []
    n=0
    for i in matrizDecodificada:
        if  i == 255 :
            if num != "":
                num = diffNull (num, decod, dic)              
            continue
        elif i == 254:
            num += "1"
        elif i == 253 :
            num += "0"
        else:
            print("numero invalido revise la codificacion")
        n += 1
    if num != "":
        num = diffNull (num, decod, dic)
    name = "Decrypt" + name + ".txt"
    #print("jghasdhas",decod)
    file = open(name, "w")
    for tx in decod:
        file.write(tx + "\n")
    file.close()
    return name
    
def comprobacion(txt1,txt2):
    primertxt = txts(txt1)
    segundotxt = txts(txt2)
    if primertxt == segundotxt:
        print("los txts son iguales")
    


def txts(archivo):
    linea=archivo.readline()
    texto = ""
    while linea != '':
        # procesar
        texto = texto + linea
        linea=archivo.readline()
        texto = texto.rstrip('\n')
    string = texto
    return string