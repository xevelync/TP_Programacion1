import random

puntaje_inicial = 100
apuesta = 10
jugar = True
caracteres_posibles = ["A", "B", "C", "D", "E", "0", "7"]

while jugar and puntaje_inicial > 0:
    print("¡BIENVENIDOS AL JUEGO TRAGAMONEDAS!")
    print("")
    print(f"Tu puntaje inicial es de: {puntaje_inicial} y tu apuesta actual de: {apuesta}")
    print("")
    print("Menú de opcines:")
    print("1. Jugar")
    print("2. Cambiar apuesta")
    print("3. Salir")
    print("")

    opcion = input("Selecciones una opción: ")
    print("")

    match opcion:
        case "1":
            if puntaje_inicial >= apuesta:
                print("EJECUTAR TIRADA")
                print("")

                primer_caracter = random.choice(caracteres_posibles)
                segundo_caracter = random.choice(caracteres_posibles)
                tercer_caracter = random.choice(caracteres_posibles)

                print(f"Resultados: {primer_caracter} | {segundo_caracter} | {tercer_caracter}")
                print("")

                if primer_caracter == "0" and segundo_caracter == "0" and tercer_caracter == "0":
                    puntaje_inicial = 0
                    print(f"¡Perdiste todos los puntos acumulado!")
                    print("¡JUEGO TERMINADO!")
                    print("")

                elif primer_caracter == "7" and segundo_caracter == "7" and tercer_caracter == "7":
                    puntos_ganados = apuesta * 10
                    puntaje_inicial += puntos_ganados
                    print(f"FELICIDADES! TRIPLE 7. Ganaste {puntos_ganados} puntos!")
                    print("")

                elif primer_caracter == segundo_caracter and primer_caracter == tercer_caracter and primer_caracter in ['A', 'B', 'C', 'D']:
                    puntos_ganados = apuesta * 5
                    puntaje_inicial += puntos_ganados
                    print(f"Felicidades! TRES IGUALES. Ganaste {puntos_ganados} puntos!.")
                    print("")

                elif primer_caracter == segundo_caracter or primer_caracter == tercer_caracter or segundo_caracter == tercer_caracter:
                    puntos_ganados = apuesta * 2
                    puntaje_inicial += puntos_ganados
                    print(f"Felicidades! DOS CARACTERES IGUALES. Ganaste {puntos_ganados} puntos!.")
                    print("")

                else:
                    puntaje_inicial -= apuesta
                    print(f"TODOS DISTINTOS! Suerte la proxima, perdiste {apuesta} puntos.")
                    print("")

            else:
                print("PUNTAJE INSUFICINTE. Ingresar nueva apuesta o salir del juego")
                break

        case "2":
            print("CAMBIAR APUESTA")
            print("")
            print(f"Tu puntaje actual es de: {puntaje_inicial}")
            print("")
            print(f"Tu apuesta actual es de: {apuesta}")
            print("")

            cambiar_apuesta = True

            while cambiar_apuesta == True:
                nueva_apuesta = int(input("Ingresar nueva apuesta: "))
                print("")

                if nueva_apuesta < 1:
                    print("ERROR! Tu apuesta debe ser mayor a 0. Ingresar nuevamente.")

                elif nueva_apuesta > puntaje_inicial:
                    print("ERROR! Tu apuesta supera el tu puntaje disponible. Ingresar nuevamente.")
                
                elif nueva_apuesta > 0 and nueva_apuesta <= puntaje_inicial:
                    apuesta = nueva_apuesta
                    print(f"APUESTA CAMBIADA CORRECTAMENTE! Tu apuesta actual es: {apuesta}")
                    print("")
                    break

                else:
                    print("ERROR. Igrese un numero entero VALIDO!")

        case "3":
            print(f"GRACIAS POR JUGAR. TUS PUNTOS SON: {puntaje_inicial}")
            jugar = False

        case _:
            print("OPCION INVALIDA, INGRESAR NUEVAMENTE")
            print("")