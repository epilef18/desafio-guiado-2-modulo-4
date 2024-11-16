class Personaje:

    def __init__(self, nombre):
        """
        Metodo constructor de la clase Personaje
        Inicia el nombre, el nivel en 1 y la experiencia en 0
        """
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        """
        Método getter del estado del personaje
        Retorna:
        String: Nombre, nivel y experiencia del personaje
        """
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp):
        """
        Metodo setter de la experiencia del personaje
        Incluye la lógica de los niveles del personaje
        Cada 100 puntos de experiencia, sube un nivel
        Si la experiencia total es negativa, el nivel baja
        Asigna la experiencia restante de la interacción con el nivel al personaje
        """
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp += 100
                self.nivel -= 1
            elif self.nivel == 1:
                tmp_exp = 0

        self.experiencia = tmp_exp

    def __lt__(self, other):
        """Sobrecarga de método __lt__
        Permite usar el operando "<" entre objetos
        """
        return self.experiencia < other.experiencia

    def __gt__(self, other):
        """Sobrecarga de método __gt__
        Permite usar el operando ">" entre objetos
        """
        return self.experiencia > other.experiencia

    def __eq__(self, other):
        """Sobrecarga de método __eq__
        Permite usar el operando "==" entre objetos
        """
        return self.experiencia == other.experiencia

    def get_probabilidad_ganar(self, other):
        """
        Método que compara los niveles de los personajes y determina la probabilidad de ganar contra el oponente "orco"
        Retorna:
        Float: Probabilidad de ganar contra el otro personaje
        """
        if self.nivel < other.nivel:
            return 0.33
        elif self.nivel > other.nivel:
            return 0.66
        else:
            return 0.50

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        """
        Método que muestra el diálogo y las opciones que tienes para jugar
        Muestra la probabilidad de ganar contra el oponente "orco" y los valores de experiencia si se gana o se pierde
        Incluye una opción para comabtir y una opcion de huida para terminar de ejecutar el programa
        """
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganar contra el Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
