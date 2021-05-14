from pruebahuf import Code_Huf
from sustituir import getDiccionario
from sustituir import sustituir
from imagenCodificada import codImg
from decodificacion import decodHuff
import cv2

def Encript(img):
    doc = open("secuenciaSherlock.txt")
    cod,freq,strIng,Longitud,Eficiencia=Code_Huf(doc)
    dic=getDiccionario(freq,cod)
    list = sustituir(dic,strIng)  
    vector_cod=codImg(img,list)  
    return Longitud, Eficiencia, dic, list
def Decrypt(img,dic,name):    
    #print("La decodificacion de la imagen es: " + str(sms))
    decodHuff(img, dic,name)
    
#l,e,d = Sherlock()