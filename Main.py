from pruebahuf import Code_Huf
from sustituir import getDiccionario
from sustituir import sustituir
from imagenCodificada import codImg
from decodificacion import decodHuff
from decodificacion import comprobacion
import cv2

def Encript(img, doc, title):
    
    cod,freq,strIng,Longitud,Eficiencia=Code_Huf(doc)
    dic=getDiccionario(freq,cod)
    list = sustituir(dic,strIng)
    tit = codImg(img,list,title)  
    return Longitud, Eficiencia, dic, list, tit

def Decrypt(img,dic,name,txt1):    
    #print("La decodificacion de la imagen es: " + str(sms))
    txt2 = decodHuff(img, dic, name)
    doc = open(txt2)
    comprobacion(txt1,doc)

def Decrypt2(img,dic,name):    
    #print("La decodificacion de la imagen es: " + str(sms))
    txt2 = decodHuff(img, dic, name)

    
#l,e,d = Sherlock()