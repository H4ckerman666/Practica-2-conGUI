#Búsca "valueToFind" dentro de "lista" y retorna el valor de su códificación
def searchValue(valueToFind, lista):
    for key in lista:
        if valueToFind == key:
            return lista[key]

# la funcion recibe como parametro la frecuencia, la codificación de huffman
def getDiccionario(frecuency, huffman_code):
    # se crea un diccionario con los datos d frecuencia y la codificación
    # la clave es la letra y el valor el código. Ejemplo:
    # {'c': 0010}
    valores = {}
    for id, char in enumerate(frecuency):
        valores[char[0]] = huffman_code[id]
    return valores

#recibe como paramtro el diccionario generado en la función "getDiccionario" y el string original
def sustituir(valores, string):
    index = 0
    length = 0
    newString = {}
    # recorremos l string original
    lista = []
    for value in string:
        # obtenemos el código Huffman de esa letra
        code = searchValue(value, valores)
        # obtenemos la longitud del código y lo sumamos al acumulador de longitud
        length += len(code)
        # Creamos un diccionario con la siguiente estructura
        # {
        #     0: Posición de la letra en el string original
        #     {
        #         'letra': 'codificación de huffman'
        #         'e': '01'
        #     }
        # }
        newString[index] = {value: code}
        lista.append(code)
        index += 1

    # Retornamos los valores del string y la longitud
    return lista
