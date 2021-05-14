import PySimpleGUI as sg
import math
import sys
import cv2
from Main import Sherlock
global probabilities


#GUI
#GUI

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Cargar secuencia Sherlock ')],
            [sg.Text('ó')],
            [sg.Text('Inserta su frase a codificar'), sg.InputText("inserte texto")],
            [sg.Button('Cargar Sherlock'),sg.Button('Cargar Frase'), sg.Button('Limpiar')],
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
    if event == "Cargar Frase":
        inputt = values[0]
        string = inputt

        freq = {}
        for c in string:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        length = len(string)

        probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
        probabilities = sorted(probabilities, reverse=True)
        print(probabilities)

        huffmanClassObject = HuffmanCode(probabilities)
        P = probabilities

        huffman_code = huffmanClassObject.compute_code()

        entRopia = huffmanClassObject.entropy_of_code(probabilities)
        print(' Caracter | Código Huffman  ')
        title = 'Caracter | Código Huffman  '
        window['TITLE'].update(value = title)

        print('----------------------')

        for id,char in enumerate(freq):
            index = "CHAR" + str(id)
            if huffman_code[id]=='':
                print(' %-4r |%12s' % (char[0], 1))

                continue
            print(' %-4r |%12s' % (char[0], huffman_code[id]))
            printt = (' %-4r |%12s' % (char[0], huffman_code[id]))
            window[index].update(value = printt)


        Long_media, En_tropia =huffmanClassObject.characteristics_huffman_code(huffman_code,entRopia)
        window['_LONGMEDIA_'].update(value = Long_media)
        window['_ENTROPIA_'].update(value = En_tropia)


    #Carga Sherlock     
    elif event == "Cargar Sherlock" :
        window['TITLE'].update(value = 'Caracter | Código Huffman  ')
        img= cv2.imread('SherlockToWatson.png',-1)
        Long_media,En_tropia,dicc,listt = Encript(img)
        print('----------------------')
        print(len(dicc))
        keys = list(dicc.keys())
        valores = list(dicc.values())
        for id in range(len(dicc)):
            index = "CHAR" + str(id)
            printt = (' %-4r |%12s' % (keys[id], valores[id]))             
            window[index].update(value = printt)        
        window['_LONGMEDIA_'].update(value = Long_media)
        window['_ENTROPIA_'].update(value = En_tropia)


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