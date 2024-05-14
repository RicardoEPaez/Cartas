import random

#Generacion  de mazo ordenado
pintas = ['trebol', 'diamante', 'pica', 'corazon']
mazo_ordenado = [f'{numero} de {pinta}' for pinta in pintas for numero in range(1,14)]

#Generacion de mazo barajeado
mazo_barajado = []         
pos_max = 52
for i in range(0,pos_max):
   num_aleatorio = random.randint(0,pos_max - 1)
   mazo_barajado.append(mazo_ordenado[num_aleatorio])
   mazo_ordenado.pop(num_aleatorio)
   pos_max -= 1

#Inicializacion de variables
puntos_jugador = 0
puntos_computadora = 0
mazo_mostrado = []



#Mostrar primera carta
carta_mostrada = mazo_barajado.pop(0)
mazo_mostrado.append(carta_mostrada)
print(f'Carta actual: {carta_mostrada}')

#Bucle de juego (resto de cartas)
while mazo_barajado:
    carta_mostrada = mazo_barajado.pop(0)
    mazo_mostrado.append(carta_mostrada)
    entrada_usuario = input('Escriba "batalla" si desea en la proxima carta jugar batalla: ')
    print(f'Carta actual: {carta_mostrada}')
    if entrada_usuario.lower() == 'batalla':
        if  len(mazo_mostrado) >= 2 and mazo_mostrado[-1].split(' de ')[0] == mazo_mostrado[-2].split(' de ')[0]:
            puntos_jugador += 1
            print("!BATALLA!. Has ganado un punto el jugador")
        else:
            print('No hay batalla')
    else:
        if  len(mazo_mostrado) >= 2 and mazo_mostrado[-1].split(' de ')[0] == mazo_mostrado[-2].split(' de ')[0]:
            puntos_computadora += 1
            print("!BATALLA!. Punto para la computadora")
    print(f"El puntaje acumulado del jugador es: {puntos_jugador}")
    print(f"El puntaje acumulado de la computadora es: {puntos_computadora}")
 
#Final del juego   
if puntos_jugador > puntos_computadora:
    print(f'Ha ganado el jugador con {puntos_jugador} puntos')
elif puntos_jugador < puntos_computadora:
    print(f"Ha ganado la computadora con {puntos_computadora} puntos")
else:
    print(f"Ha habido un empate con {puntos_jugador}")
    
