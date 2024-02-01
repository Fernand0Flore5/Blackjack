import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartas = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(self.cartas)

    def dar_carta(self):
        return self.cartas.pop()

class Jugador:
    def __init__(self, nombre, saldo_inicial=100):
        self.nombre = nombre
        self.cartas = []
        self.saldo = saldo_inicial
        self.apuesta = 0

    def recibir_carta(self, carta):
        self.cartas.append(carta)

    def calcular_puntaje(self):
        puntaje = 0
        ases = 0

        for carta in self.cartas:
            if carta.valor.isdigit():
                puntaje += int(carta.valor)
            elif carta.valor in ['J', 'Q', 'K']:
                puntaje += 10
            elif carta.valor == 'A':
                puntaje += 11
                ases += 1

        while puntaje > 21 and ases:
            puntaje -= 10
            ases -= 1

        return puntaje
    
    def elegir_valor_ases(self):
        for i, carta in enumerate(self.cartas):
            if carta.valor == 'A':
                while True:
                    try:
                        valor_as = int(input(f"¿Qué valor quieres para el As en {carta.palo}? (1/11): "))
                        if valor_as in [1, 11]:
                            self.cartas[i].valor = str(valor_as)
                            break
                        else:
                            print("Por favor, ingresa 1 o 11.")
                    except ValueError:
                        print("Por favor, ingresa un número válido.")

class Blackjack:
    
    def repartir_cartas_iniciales(self):
        self.jugador.apuesta = 0

        # Realizar apuesta del jugador
        while True:
            try:
                apuesta = int(input(f"{self.jugador.nombre}, ¿cuánto quieres apostar? (Saldo actual: {self.jugador.saldo}): "))
                if 0 < apuesta <= self.jugador.saldo:
                    self.jugador.apuesta = apuesta
                    self.jugador.saldo -= apuesta
                    break
                else:
                    print("Cantidad no válida. Asegúrate de tener suficiente saldo.")
            except ValueError:
                print("Por favor, ingresa una cantidad válida.")

    def __init__(self):
        self.mazo = Mazo()
        self.jugador = Jugador("Jugador")
        self.crupier = Jugador("Crupier")

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            carta_jugador = self.mazo.dar_carta()
            self.jugador.recibir_carta(carta_jugador)
            carta_crupier = self.mazo.dar_carta()
            self.crupier.recibir_carta(carta_crupier)

        self.jugador.elegir_valor_ases()  # Nueva línea
        self.crupier.elegir_valor_ases()  # Nueva línea

    def mostrar_cartas(self, jugador, ocultar_primera=False):
        cartas = jugador.cartas if not ocultar_primera else [jugador.cartas[0], '???']
        print(f"{jugador.nombre}: {', '.join(str(carta) for carta in cartas)}")

    def jugar(self):
        print("¡Bienvenido al juego de Blackjack!")

        self.repartir_cartas_iniciales()
        self.mostrar_cartas(self.jugador)
        self.mostrar_cartas(self.crupier, ocultar_primera=True)

        while True:
            opcion = input("¿Quieres tomar otra carta? (s/n): ").lower()

            if opcion == 's':
                nueva_carta = self.mazo.dar_carta()
                self.jugador.recibir_carta(nueva_carta)
                self.jugador.elegir_valor_ases()  # Llamar después de recibir cada nueva carta
                self.mostrar_cartas(self.jugador)

                if self.jugador.calcular_puntaje() > 21:
                    print("¡Te has pasado de 21! Has perdido.")
                    break
            elif opcion == 'n':
                while self.crupier.calcular_puntaje() < 17:
                    self.crupier.recibir_carta(self.mazo.dar_carta())
                self.mostrar_cartas(self.crupier)

                jugador_puntaje = self.jugador.calcular_puntaje()
                crupier_puntaje = self.crupier.calcular_puntaje()

                if jugador_puntaje > 21:
                    print("Has perdido.")
                elif crupier_puntaje > 21 or jugador_puntaje > crupier_puntaje:
                    print("¡Felicidades! Has ganado.")
                    self.jugador.saldo += self.jugador.apuesta * 2
                elif jugador_puntaje == crupier_puntaje:
                    print("Empate.")
                    self.jugador.saldo += self.jugador.apuesta
                else:
                    print("Has perdido.")
                break
            else:
                print("Opción no válida. Por favor, ingresa 's' o 'n'.")
                
        print(f"Saldo actual de {self.jugador.nombre}: {self.jugador.saldo}")
        
    def reiniciar_juego(self):
        self.mazo = Mazo()
        self.jugador = Jugador("Jugador")
        self.crupier = Jugador("Crupier")
        self.jugar()

if __name__ == "__main__":
    juego = Blackjack()
    juego.jugar()

    while input("¿Quieres jugar de nuevo? (s/n): ").lower() == 's':
        if  self.jugador.saldo == 0:
                
            print("Te has quedado sin dinero. ¡Gracias por jugar!")
            break
         
        print("")
        juego.reiniciar_juego()
        