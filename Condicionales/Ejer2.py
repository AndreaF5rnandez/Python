#Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores 
# un programa en Python que dado el tamaño de un pez indique si su organismo está 
# contaminado. Para ello tendremos 4 opciones:

#Tamaño Normal: Mensaje "Pez en buenas condiciones"

#Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

#Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

#Tamaño sobredimensionado: Mensaje "Pez contaminado"

TamañoNormal = int(input('Ingrese el tamaño normal que debe tener un pez: '))
TamañoSobredimensionado = int(input('Ingrese el tamano Sobresaliente :  '))
TamañoDelPez = int(input('Ingrese el tamano del pez a analizar: '))

if(TamañoNormal == TamañoDelPez):
    print('Pez en buenas condiciones')
elif(TamañoDelPez >= TamañoSobredimensionado):
    print('Pez contaminado')
elif(TamañoDelPez < TamañoNormal):
    print("Pez con problemas de nutrición")
else:
    print("Pez con síntomas de organismo contaminado")

    