import PySimpleGUI as sg
from tkinter import messagebox
from tkinter import filedialog
import math
import os
import pickle
import cv2
import pandas as pd
import csv
import ntpath
from Main import Encript
from Main import Decrypt
from Main import Decrypt2
global probabilities


#GUI
#GUI

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Cargar secuencia Sherlock ')],
            [sg.Text('ó')],
            [sg.Text('Inserta su frase a codificar'), sg.InputText("inserte texto")],
            [sg.Button('Encriptar Sherlock'),sg.Button('Desencryptar Sherlock'),sg.Button('Encriptar tus archivos'),sg.Button('Desencriptar tu imagen'), sg.Button('Limpiar')],
            [sg.Text('',size=(50,1), key = 'TITLE')],
            [sg.Text('',size=(50,1), key = 'CHAR0')],
            [sg.Text('',size=(50,1), key = 'CHAR1')],
            [sg.Text('',size=(50,1), key = 'CHAR2')],
            [sg.Text('',size=(50,1), key = 'CHAR3')],
            [sg.Text('',size=(50,1), key = 'CHAR4'), sg.Text('',size=(50,1), key = '_LONGMEDIA_')],
            [sg.Text('',size=(50,1), key = 'CHAR5'), sg.Text('',size=(50,1), key = '_ENTROPIA_')],
            [sg.Text('',size=(50,1), key = 'CHAR6')],
            [sg.Text('',size=(50,1), key = 'CHAR7')],
            [sg.Text('',size=(50,1), key = 'CHAR8')],
            [sg.Text('',size=(50,1), key = 'CHAR9')],
            [sg.Text('',size=(50,1), key = 'CHAR10')],
            [sg.Text('',size=(50,1), key = 'CHAR11')],
            [sg.Text('',size=(50,1), key = 'CHAR12')],
            [sg.Text('',size=(50,1), key = 'CHAR13')],
            [sg.Text('',size=(50,1), key = 'CHAR14')],
            [sg.Text('',size=(50,1), key = 'CHAR15')],
            [sg.Text('',size=(50,1), key = 'CHAR16')],
            [sg.Text('',size=(50,1), key = 'CHAR17')],
            [sg.Text('',size=(50,1), key = 'CHAR18')],
            [sg.Text('',size=(50,1), key = 'CHAR19')],
            [sg.Text('',size=(50,1), key = 'CHAR20')],
            
            
             ]

# Create the Window
window = sg.Window('Codificación Huffman', layout)
#window.geometry("1000x700")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == "Encriptar tus archivos":
        
        archivo=filedialog.askopenfilename(title="Elije tu imagen")
        archivo2=filedialog.askopenfilename(title="Elije tu mensaje a codificar")
        window['TITLE'].update(value = 'Caracter | Código Huffman  ')
        archivo_name = ntpath.basename(archivo)
        archivo_name = archivo_name.split(".")

        img= cv2.imread(archivo,-1)
        
        title = archivo_name[0]
        doc = open(archivo2)
        Long_media,En_tropia,dicc,listt,im2 = Encript(img,doc,title)
        keys = list(dicc.keys())
        valores = list(dicc.values())
        for id in range(len(dicc)):
            index = "CHAR" + str(id)
            printt = (' %-4r |%12s' % (keys[id], valores[id]))             
            window[index].update(value = printt)
        
        name_dic = "dic" + title + ".dat"
        with open(name_dic, "wb") as f:
            pickle.dump(dicc, f)    
        window['_LONGMEDIA_'].update(value = Long_media)
        window['_ENTROPIA_'].update(value = En_tropia)
        messagebox.showinfo(title="Listo!!",message="Encriptacion Exitosa, imagen generada")



    #Carga Sherlock     
    elif event == "Encriptar Sherlock" :
        window['TITLE'].update(value = 'Caracter | Código Huffman  ')
        img= cv2.imread('SherlockToWatson.png',-1)
        doc = open("secuenciaSherlock.txt")
        title = "SherlockToWatson2"
        Long_media,En_tropia,dicc,listt,im2 = Encript(img,doc,title)        
        keys = list(dicc.keys())
        valores = list(dicc.values())
        name_dic = "dic" + title + ".dat"
        for id in range(len(dicc)):
            index = "CHAR" + str(id)
            printt = (' %-4r |%12s' % (keys[id], valores[id]))

            window[index].update(value = printt)  

        with open(name_dic, "wb") as f:
            pickle.dump(dicc, f)    
        



        window['_LONGMEDIA_'].update(value = Long_media)
        window['_ENTROPIA_'].update(value = En_tropia)
        messagebox.showinfo(title="Listo!!",message="Encriptacion Exitosa, imagen generada")
        
    elif event == "Desencryptar Sherlock" :
        txt1 = open("secuenciaSherlock.txt")
        name = "secuenciaSherlock"
        img2= cv2.imread(im2,-1)
        Decrypt(img2,dicc,name,txt1)
        messagebox.showinfo(title="Listo!!",message="Desencriptacion Exitosa, txt generado, SON IDENTICOS")
        
    elif event == "Desencriptar tu imagen" :
        archivo=filedialog.askopenfilename(title="Elije tu imagen a desencriptar")
        archivo2=filedialog.askopenfilename(title="Elije su diccionario para desencriptar")

        archivo_name = ntpath.basename(archivo)
        archivo_name = archivo_name.split(".")
        name = archivo_name[0]

        img2= cv2.imread(archivo,-1) 
        txt1 = open(archivo2)

        with open(archivo2, "rb") as f:
            dicc = pickle.load(f)   


        Decrypt2(img2,dicc,name)
        messagebox.showinfo(title="Listo!!",message="Desencriptacion Exitosa")


        #LIMPIAR TEXT
    elif event == "Limpiar" :
            window['TITLE'].update(value = "")
            window['CHAR0'].update(value = "")
            window['CHAR1'].update(value = "")
            window['CHAR2'].update(value = "")
            window['CHAR3'].update(value = "")
            window['CHAR4'].update(value = "")
            window['CHAR5'].update(value = "")
            window['CHAR6'].update(value = "")
            window['CHAR7'].update(value = "")
            window['CHAR8'].update(value = "")
            window['CHAR9'].update(value = "")
            window['CHAR10'].update(value = "")
            window['CHAR11'].update(value = "")
            window['CHAR12'].update(value = "")
            window['CHAR13'].update(value = "")
            window['CHAR14'].update(value = "")
            window['CHAR15'].update(value = "")
            window['CHAR16'].update(value = "")
            window['CHAR17'].update(value = "")
            window['CHAR18'].update(value = "")
            window['CHAR19'].update(value = "")
            window['CHAR20'].update(value = "")
            window['_LONGMEDIA_'].update(value = "")
            window['_ENTROPIA_'].update(value = "")



#GUI
#GUI