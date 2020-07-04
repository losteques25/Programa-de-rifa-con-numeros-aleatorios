import sys
import random
sigo_ejecutando = "S"


numero=int(random.uniform(1,9))#el numero a acertar
#print(numero)
#print()
intentos=0 # para decirle a la maquina que arranque desde cero.
lintentos=3 # La cantidad de oportunidades del jugador
print("*** Selecciona un numero del 1 al 9**** ")   
print("*** Solo tienes tres oportunidades de ganar***")
while intentos<lintentos:
    print()
    adivina=int(input("Adivina el numero:    "))
    print()
    intentos += 1 # el contador
    if adivina==numero: 
        print("Felicitaciones. Ganastes un millon de dolares")
        break
    if adivina > numero:
        print("Introdujo Valor Superior al buscado")  # Mensaje valor superior
    if adivina < numero:
        print("Introdujo Valor Inferior al buscado")  # Mensaje valor inferior
    if intentos == lintentos:  # Para usar con continue y seguir intentando
        print()
        print("Lo sentimos. Será la proxima vez completo sus 3 intentos")
        print()
        sigo_ejecutando = input('"Sigo intentando S/N:" ')
        if sigo_ejecutando == "N" or sigo_ejecutando == "n":
            print("Salgo")
            sys.exit()   # Para terminar el programa.
        if sigo_ejecutando == "S" or sigo_ejecutando == "s":
            intentos = 0   # El contador de intentos lo igualo a 0 o reinicio, si
                           # no se sale en el while
            continue   #Para regresar al principio del bucle o loop

