def conversacion(mensaje):
    print('Hola\nCómo estás')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opción (1,2,3): '))

if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegista la opción 3')
else:
    print('Escribe la opción correcta')


def suma(a,b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado # para retornar un valor

sumatoria = sum(1,4)
print(sumatoria)