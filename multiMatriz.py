print("Ingrese las dimensiones de la primera matriz")
filA=int(input("Ingrese la fila de la primera matriz: "))

colA=int(input("Ingrese la columna de la primera matriz: "))

print("Ingrese las dimensiones de la primera matriz")
filB=int(input("Ingrese la fila de la segunda matriz: "))

colB=int(input("Ingrese la columna de la segunda matriz: "))

#LLenado de matrices con ceros
matrizA = []
for i in range(filA):
	matrizA.append([0]*colA)

matrizB = []
for i in range(filB):
	matrizB.append([0]*colB)

#Ingreso de los valores de cada matriz
print("Ingrese los valores de la matriz A: ")	
for i in range(filA):
	for j in range(colB):
		matrizA[i][j] = int(input( ))
#Matriz B	
print("Ingrese los valores de la matriz B: ")	
for i in range(filB):
	for j in range(colB):
		matrizB[i][j] = int(input( ))
	

#Impresión matrices
for i in matrizA:
	for j in i:
		print (j),
	print

	

for i in matrizB:
	for j in i:
		print (j),
	print
	

#Multiplicación de matrices
mresultado = []
q=0

#m1[m][n]*m2[x][y]=m3[m][y] n = x
while q < 1:
	if colA == filB:
		print("La multiplicación de las matrices es: ")
		
		for i in range(filA):
			mresultado.append([0]*colB)
		
		for i in range(filA):
			for j in range(colB):
				for x in  range(colA):
					mresultado[i][j]+=matrizA[i][x]*matrizB[x][j]

		for i in mresultado:
			for j in i:
				print (j),
			print
				
		q+=1
		
	else :
		print("No se puede multiplicar las dos matrices.")
		
#Matriz traspuesta
matriz = []
for i in range(colA):
	mresultado.append([0]*filA)

#asignación y traspuesta
for i in range(filA):
        
        for j in range(colA):
                mresultado[j][i]=matrizA[i][j] #traspone lo valores de filas y columnas
print ("La matriz traspuesta es: ")
for i in matriz:
        print(i)
#Suma de las matriz
for i in range (filA)
	for j in range(colA)
		matrizSuma[i][j]= matrizA[i][j] + matrizB[i][j]
print ("La suma de la matriz es: ")
print matrizSuma	
