import cv2 
#Pasa 0 1 espacio a numeros asignados
def aNumeros(codigo):
	c= []
	for m in codigo:
		for k in m:
			if k == '1':
				c.append(254)
			if k == '0':
				c.append(253)
		c.append(255)
	return c

def codImg(imagen,code,title):
	a = imagen[:,:,3]
	b = imagen[:,:,0]
	g = imagen[:,:,1]
	r = imagen[:,:,2]
	ancho = len(a)
	alto = len(a[0])
	vectorCodificado = aNumeros(code)
	#print(vectorCodificado)
	comprobar = (alto * ancho) - len(code)
	#print(comprobar)
	#print("-----")
	v= a.flatten() #Vector unidimencional
	#LLena los primeros pixeles de la componente a
	for k in range(0,len(vectorCodificado)):
		v[k] = vectorCodificado[k] 
	newComponetA= v.reshape(ancho,alto)
	#Combina rgb y su la nueva componenete
	newImage = cv2.merge((b,g,r,newComponetA))
	title += ".png" 
	cv2.imwrite(title,newImage)
	print("Se ah generado la imagen con el nombre ImagenEncriptada.png")
	cv2.waitKey(0)
	return title


 