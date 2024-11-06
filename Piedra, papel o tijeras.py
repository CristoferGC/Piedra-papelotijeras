import numpy as np

import time





def piedra_tijera_papel():
    #las opciones asignadas a lo que vencen
    opciones = {'piedra': 'tijeras', 'tijeras':'papel', 'papel': 'piedra'}
    #entrada del jugador
    jugador = input("Escribe piedra, papel o tijeras: ")
    while jugador not in {'piedra', 'papel', 'tijeras'}:
        print('Te equivocaste al escribir')
        jugador = input ("Escribe piedra, papel o tijeras: ")
        #Selección aleatoria para la computadora
    computadora = np.random.choice(['piedra', 'papel', 'tijeras'])
    #mostrar las selecciones
    time.sleep(.5)
    print("\nHas seleccionado: ", jugador)
    print("La computadora ha seleccionado: ", computadora, '\n')
    time.sleep(2)
    #determinar el ganador
    if opciones[jugador] == computadora:
        print("Has ganado")
    elif opciones[computadora] == jugador:
        print("Has perdido")
    else:
        print("Empate, trata de nuevo")

piedra_tijera_papel()