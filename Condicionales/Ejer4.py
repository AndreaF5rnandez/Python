#La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al 
# nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

#La sección A esta formada por los barrios céntricos cuyo nombre comienza con una 
# letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la 
# sección B el resto.

#Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe 
# en que sección se encuentra.

nombreDelBarrio = str(input('Ingrese el nombre del barrio: '))
print('La ubicaion del barrio pude ser <Centrico> <No centrico>')
ubicacion = str(input('Ingrese la ubicaion del barrio: '))

nombresDeLaSeccionA = ['L','N']

if( (nombreDelBarrio[0] in nombresDeLaSeccionA) and (ubicacion == 'Centrico')):
    print('Se encuentra en la Seccion A')
elif ((nombreDelBarrio[0] not in nombresDeLaSeccionA) and (ubicacion == 'No Centrico')):
    print('Se encuentra en la Seccion B')
else: 
    print('Nose encuentra en ninguna Seccion o escribio mal los datos')