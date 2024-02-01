import random                                                                               #Se importa el modulo random

class Carta:                                                                                #Se define la clase Carta
    def __init__(self, valor, palo):                                                        # Constructor de la clase Carta,se llama cuando se crea una nueva carta                                  
        self.valor = valor            
        self.palo = palo                                                                    # Establece los atributos iniciales de la carta: valor y palo

        
    def __str__(self):
        return f"{self.valor}{self.palo}"                                                   # Función especial llamada cuando se intenta convertir una carta a cadena, devuelve una representación en cadena de la carta, incluyendo su valor y palo

class Mazo:                                                                                 #Se define la clase Mazo
    def __init__(self):
        palos = ['♥', '◆', '♠', '♣']      
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']        # Constructor de la clase Mazo, crea un mazo de cartas, baraja las cartas y las guarda en el atributo cartas
        self.cartas = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(self.cartas)

    def dar_carta(self):
        return self.cartas.pop()                                                            # Devuelve la carta superior del mazo (carta aleatoria) y la elimina del mazo

class Jugador:
    def __init__(self, nombre):                                                             # Constructor de la clase Jugador, se llama al crear un nuevo jugador, establece el nombre del jugador y crea una lista para sus cartas
        self.nombre = nombre                                                                
        self.cartas = []

    def recibir_carta(self, carta):                                                         # Añade una carta a la lista de cartas del jugador
        self.cartas.append(carta)

    def calcular_puntaje(self):
        puntaje = 0                                                                         # Calcula y devuelve el puntaje total del jugador
        ases = 0

        for carta in self.cartas:
            if carta.valor.isdigit():                                                       #La función isdigit() en Python es un método de las cadenas de caracteres (str) y se utiliza para verificar si todos los caracteres en una cadena son dígitos numéricos. Retorna True si todos los caracteres son dígitos y False si la cadena contiene al menos un carácter que no es un dígito
                puntaje += int(carta.valor)
            elif carta.valor in ['J', 'Q', 'K']:                                            # Ajusta el valor de los ases si el puntaje es mayor a 21
                puntaje += 10
            elif carta.valor == 'A':
                puntaje += 11
                ases += 1

        while puntaje > 21 and ases:
            puntaje -= 10
            ases -= 1

        return puntaje

class Blackjack:                                                                             #Se define la clase Blackjack
    def __init__(self):
        self.mazo = Mazo()
        self.jugador = Jugador("Jugador")                                                    # Constructor de la clase Blackjack, Crea una instancia de Mazo, y dos instancias de jugador y crupier
        self.crupier = Jugador("Crupier")

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            self.jugador.recibir_carta(self.mazo.dar_carta())                                # Reparte dos cartas a cada jugador al inicio del juego
            self.crupier.recibir_carta(self.mazo.dar_carta())

    def mostrar_cartas(self, jugador, ocultar_primera=False):
        cartas = jugador.cartas if not ocultar_primera else [jugador.cartas[0], '???']       # Muestra las cartas del jugador o crupier, si ocultar_primera es True, oculta la primera carta del crupier
        print(f"{jugador.nombre}: {', '.join(str(carta) for carta in cartas)}")

    def jugar(self):                                                                         # Función principal que inicia y controla el juego de Blackjack
        print("¡Bienvenido al juego de Blackjack!")

        self.repartir_cartas_iniciales()
        self.mostrar_cartas(self.jugador)                                                     
        self.mostrar_cartas(self.crupier, ocultar_primera=True)

        while True:
            opcion = input("¿Quieres tomar otra carta? (s/n): ").lower()

            if opcion == 's':                                                                # El jugador toma otra carta
                self.jugador.recibir_carta(self.mazo.dar_carta())
                self.mostrar_cartas(self.jugador)

                if self.jugador.calcular_puntaje() > 21:
                    print("¡Te has pasado de 21! Has perdido.")
                    break
            elif opcion == 'n':                                                              # El jugador se queda con las cartas actuales y se revelan las cartas del crupier
                while self.crupier.calcular_puntaje() < 17:
                    self.crupier.recibir_carta(self.mazo.dar_carta())
                self.mostrar_cartas(self.crupier)

                if self.crupier.calcular_puntaje() > 21 or self.jugador.calcular_puntaje() > self.crupier.calcular_puntaje():
                    print("¡Felicidades! Has ganado.")
                elif self.jugador.calcular_puntaje() == self.crupier.calcular_puntaje():     # Determinar el resultado del juego
                    print("Empate.")
                else:
                    print("Has perdido.")
                break
            else:
                print("Opción no válida. Por favor, ingresa 's' o 'n'.")

if __name__ == "__main__":                                                                    # Crea una instancia del juego de Blackjack y llama a la función jugar para comenzar el juego,  )Código que se ejecutará solo si este script se ejecuta directamente)
    juego = Blackjack()                                                                         
    juego.jugar()