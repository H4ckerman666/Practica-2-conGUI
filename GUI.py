import PySimpleGUI as sg
import math
import sys
global probabilities
probabilities = []



class HuffmanCode:
    def __init__(self,probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1
    def entropy_of_code(self, prob):
        probabilidades = prob [:]
        entropia = 0
        for i in probabilidades:
            entropia = entropia + (i)*math.log((1/i),2)
        return entropia

    def characteristics_huffman_code(self, code,entropy):
        length_of_code = [len(k) for k in code]

        mean_length = sum([a*b for a, b in zip(length_of_code, self.probability)])

        print("Longitud media del código: %f" % mean_length)
        LM = ("Longitud media del código: %f" % mean_length)
        print("Eficiencia del código: %f" % ((entropy/mean_length)*100) + "%" )
        ENT = ("Eficiencia del código: %f" % ((entropy/mean_length)*100) + "%" )
        return LM, ENT

    def compute_code(self):
        num = len(self.probability)
        huffman_code = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman_code[num-i-1] != '' and huffman_code[num-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[num-i-1] != ''):
                huffman_code[num-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[num-i-2] != ''):
                huffman_code[num-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num-i-1] = '1'
                huffman_code[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[num-i-2], list) and isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + huffman_code[num-i-2]
            elif(isinstance(huffman_code[num-i-2], list)):
                complete_code = huffman_code[num-i-2] + [huffman_code[num-i-1]]
            elif(isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + [huffman_code[num-i-2]]
            else:
                complete_code = [huffman_code[num-i-2], huffman_code[num-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

#GUI
#GUI

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Cargar secuencia Sherlock ')],
            [sg.Text('ó')],
            [sg.Text('Inserta su frase a codificar'), sg.InputText("inserte texto")],
            [sg.Button('Cargar Sherlock'),sg.Button('Cargar Frase'), sg.Button('Limpiar')],
            [sg.Text('',size=(50,1), key = 'TITLE'), ],
            [sg.Text('',size=(50,1), key = 'CHAR0'), ],
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
        archivo = open("secuenciaSherlock.txt")
        linea=archivo.readline()
        texto = ""

        while linea != '':

            # procesar línea
            texto = texto + linea
            linea=archivo.readline()
            texto = texto.rstrip('\n')

        print(texto)  

        string = texto

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
            $sadas



#GUI
#GUI