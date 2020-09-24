#numero = int(input('Bienvenido, programa que genera potencias hasta 1000\nIngresa un numero: '))

#for n in range(10):
#    print('El numero '+str(numero)+' elevado a '+str(n)+' es igual a: '+str(numero**n))

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: 
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()