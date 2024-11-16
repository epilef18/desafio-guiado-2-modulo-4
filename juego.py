from personaje import Personaje
import random


def main():
    """
    Funcion principal que presenta el juego, crea los personajes y avisa del combate al usuario.
    Permite elegir si se quiere pelear o huir.
    Luego muestra el resultado del combate

    """
    print("¡Bienvenido a Gran Fantasía!")
    nombre = input("Por favor indique el nombre de su personaje:\n")
    p = Personaje(nombre)
    print(p.estado)

    print("\n¡Oh no!, ¡Ha aparecido un Orco!")

    o = Personaje("Orco")

    probabilidad_ganar = Personaje.get_probabilidad_ganar(p, o)

    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

    while opcion_orco == 1:
        resultado = "Gana" if random.uniform(0, 1) > probabilidad_ganar else "Pierde"

        if resultado == "Gana":
            print(
                "\n¡Le has ganado al orco, felicidades!\n"
                "¡Recibirás 50 puntos de experiencia!\n"
            )
            p.estado = 50
            o.estado = -30

        elif resultado == "Pierde":
            print(
                "\n¡Oh no! ¡El orco te ha ganado!\n"
                "¡Has perdido 30 puntos de experiencia!\n"
            )
            p.estado = -30
            o.estado = 50

        print(p.estado)
        print(o.estado)

        probabilidad_ganar = p.get_probabilidad_ganar(o)
        opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

    else:
        print("\n El orco ha quedado atrás.")


main()
