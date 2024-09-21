import turtle
import random

# Función para dibujar un girasol con tamaños y colores variables
def draw_sunflower(t, x, y, size=50, petal_color="orange", center_color="brown"):
    # Dibujar los pétalos
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)  # Asegurarse de que el ángulo inicial es 0
    for i in range(36):
        t.color(petal_color)
        t.begin_fill()
        t.circle(size, steps=6)  # Pétalos hexagonales
        t.end_fill()
        t.right(10)

    # Dibujar el centro del girasol en el medio de los pétalos
    t.penup()
    t.goto(x, y - size // 1)
    t.pendown()
    t.color(center_color)
    t.begin_fill()
    t.circle(size // 1)
    t.end_fill()

# Función para dibujar tallo con hojas más realistas
def draw_stem_and_leaves(t, x, y, stem_length=200):
    # Dibujar el tallo
    t.penup()
    t.goto(x, y - 100)
    t.setheading(270)
    t.pendown()
    t.color("green")
    t.pensize(8)
    t.forward(stem_length)

    # Dibujar las hojas en el tallo
    t.pensize(2)
    for leaf_angle in [45, 315]:  # Dos hojas en ángulos diferentes
        t.penup()
        t.goto(x - 5, y - 100 - stem_length // 2)  # Las hojas salen de la mitad del tallo
        t.setheading(leaf_angle)
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(40, 180)  # Hojas curvas
        t.end_fill()

# Función para dibujar la coneja
def draw_bunny(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Dibujar el cuerpo
    t.color("gray")
    t.begin_fill()
    t.circle(50)  # Cuerpo
    t.end_fill()

    # Dibujar la cabeza
    t.penup()
    t.goto(x, y + 60)
    t.pendown()
    t.begin_fill()
    t.circle(30)  # Cabeza
    t.end_fill()

    # Dibujar las orejas
    t.penup()
    t.goto(x - 30, y + 60)
    t.pendown()
    t.begin_fill()
    t.setheading(45)
    t.circle(20, 180)  # Oreja izquierda
    t.end_fill()

    t.penup()
    t.goto(x + 20, y + 90)
    t.pendown()
    t.begin_fill()
    t.setheading(135)
    t.circle(20, -180)  # Oreja derecha
    t.end_fill()

    # Dibujar los ojos
    t.penup()
    t.goto(x - 30, y + 45)
    t.pendown()
    t.color("black")
    t.dot(5)  # Ojo izquierdo

    t.penup()
    t.goto(x - 10, y + 45)
    t.pendown()
    t.dot(5)  # Ojo derecho

    # Dibujar la nariz
    t.penup()
    t.goto(x - 20, y + 35)
    t.pendown()
    t.dot(5, "pink")  # Nariz

    # Dibujar la cola
    t.penup()
    t.goto(x - 100, y - 30)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)  # Cola
    t.end_fill()

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Crear el objeto turtle
t = turtle.Turtle()
t.speed(0)  # Velocidad máxima

# Dibujar un ramo de girasoles con diferentes tamaños y disposiciones
# Primer girasol
draw_sunflower(t, -100, 150, size=60, petal_color="gold")
draw_stem_and_leaves(t, -100, 150, stem_length=250)

# Segundo girasol
draw_sunflower(t, 0, 120, size=50, petal_color="yellow")
draw_stem_and_leaves(t, 0, 120, stem_length=220)

# Tercer girasol
draw_sunflower(t, 100, 180, size=55, petal_color="orange")
draw_stem_and_leaves(t, 100, 180, stem_length=230)

# Cuarto girasol (movido un poco más abajo)
draw_sunflower(t, -50, 70, size=45, petal_color="lightyellow")  # Y ajustado a 70
draw_stem_and_leaves(t, -50, 80, stem_length=220)

# Quinto girasol (movido un poco más abajo)
draw_sunflower(t, 70, 80, size=50, petal_color="darkorange")  # Y ajustado a 80
draw_stem_and_leaves(t, 70, 80, stem_length=210)

# Dibujar la coneja en la esquina inferior izquierda
draw_bunny(t, -200, -170)

# Agregar el texto "Buona giornata!"
t.penup()
t.goto(0, -300)  # Posicionamos el texto debajo del ramo
t.pendown()
t.color("black")
t.write("Buona giornata, mi manchi tanto!", align="center", font=("Arial", 24, "bold"))

# Ocultar la tortuga y finalizar el dibujo
t.hideturtle()

# Finalizar el programa
screen.mainloop()