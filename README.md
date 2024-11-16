# **Gran Fantasía - Juego por Comida**

Este es un prototipo de consola para el juego *Gran Fantasía*, desarrollado como parte de la iniciativa de la startup "Juegos por Comida". El juego permite a los usuarios crear un personaje, enfrentarse a un orco y tomar decisiones estratégicas para ganar experiencia y subir de nivel.

---

## **Características**

- Creación de personajes con nivel y experiencia iniciales.
- Gestión dinámica de estados de los personajes (nivel y experiencia).
- Comparación de personajes basada en niveles.
- Simulación de enfrentamientos con cálculo de probabilidades.
- Sistema de decisiones: atacar o huir.

---

## **Estructura del Proyecto**

El proyecto está compuesto por dos archivos principales:

1. **`personaje.py`**  
   Define la clase `Personaje`, que permite crear personajes y gestionar su estado.
   - **Métodos principales:**
     - **Constructor**: Inicializa el nombre, nivel y experiencia.
     - **Getter y Setter**: Para consultar y asignar experiencia.
     - **Sobrecarga de operadores**: Para comparar niveles entre personajes.
     - **Cálculo de probabilidad**: Determina las probabilidades de ganar contra otro personaje.

2. **`juego.py`**  
   Contiene el flujo principal del juego, gestionando la interacción con el usuario y los enfrentamientos.
   - **Funcionalidades principales:**
     - Solicita el nombre del jugador.
     - Crea el personaje del jugador y un "Orco".
     - Calcula probabilidades de enfrentamiento.
     - Permite atacar o huir con resultados dinámicos.

---

## **Requisitos**

- **Python 3.x** instalado.
- Módulo estándar `random` (incluido en Python).

---

## **Cómo Ejecutar el Juego**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tuusuario/gran-fantasia.git
   cd gran-fantasia
