#Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de 
# receta aparecen a continuación.

#Ingredientes comunes: Verduras y berenjena.

#Ingredientes Receta 1: Lentejas y apio.

#Ingredientes Receta 2: Morrón y Cebolla..

#Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de 
# su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo 
# se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de 
# receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

ingredientes = []
print('Hay dos tipos de recetas ecologicas 1 o 2')
tipoDeReceta = int(input('Ingrese el tipo tipo de receta que desea >>>'))

if tipoDeReceta == 1 :
    print('Ingredientes disponibles >>>>')
    print('<Verduras> <Berenjenas> <Morron> <Cebolla>')
    print('Elija 3 ingredientes')
    ingredientes.append(str(input('Ingrese el primer ingrediente: ')))
    ingredientes.append(str(input('Ingrese el segundo ingrediente: ')))
    ingredientes.append(str(input('Ingrese el tercero ingrediente: ')))
    print('Eligio el tipo de receta ecologica nro 1')
    print('Su lista de ingredientes es >>>', ingredientes)
elif tipoDeReceta == 2:
    print('Ingredientes disponibles >>>>')
    print('<Verduras> <Berenjenas> <Lentejas> <Apio>')
    print('Elija 3 ingredientes')
    ingredientes.append(str(input('Ingrese el primer ingrediente')))
    ingredientes.append(str(input('Ingrese el segundo ingrediente')))
    ingredientes.append(str(input('Ingrese el tercero ingrediente')))
    print('Eligio el tipo de receta ecologica nro 2')
    print('Su lista de ingredientes es >>>', ingredientes)
