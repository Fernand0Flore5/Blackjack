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
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []

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

class Blackjack:
    def __init__(self):
        self.mazo = Mazo()
        self.jugador = Jugador("Jugador")
        self.crupier = Jugador("Crupier")

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            self.jugador.recibir_carta(self.mazo.dar_carta())
            self.crupier.recibir_carta(self.mazo.dar_carta())

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
                self.jugador.recibir_carta(self.mazo.dar_carta())
                self.mostrar_cartas(self.jugador)

                puntaje_jugador = self.jugador.calcular_puntaje()

                if puntaje_jugador > 21:
                    diferencia_puntos = puntaje_jugador - 21
                    print(f"¡Te has pasado por {diferencia_puntos} puntos! Mala decisión. Has perdido.")
                    break
                else:
                    print("EXCELENTE DECISIÓN")
                    print(". Has recibido:", self.jugador.cartas[-1])
            elif opcion == 'n':
                while self.crupier.calcular_puntaje() < 17:
                    self.crupier.recibir_carta(self.mazo.dar_carta())
                self.mostrar_cartas(self.crupier)

                if self.crupier.calcular_puntaje() > 21 or self.jugador.calcular_puntaje() > self.crupier.calcular_puntaje():
                    print("¡Felicidades! Has ganado.")
                elif self.jugador.calcular_puntaje() == self.crupier.calcular_puntaje():
                    print("Empate.")
                else:
                    print("Has perdido.")
                break
            else:
                print("Opción no válida. Por favor, ingresa 's' o 'n'.")

if __name__ == "__main__":
    juego = Blackjack()
    juego.jugar()
