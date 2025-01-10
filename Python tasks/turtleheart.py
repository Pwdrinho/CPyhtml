import math
import turtle

def heart_x(t):
    return 11 * math.sin(t) ** 3

def heart_y(t):
    return 11 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

def draw_heart():
    turtle.speed(10)  # Velocidade máxima da tartaruga
    turtle.color('purple')  # Cor da tartaruga
    turtle.penup()  # Levanta a caneta para não desenhar ao mover para a posição inicial
    turtle.goto(heart_x(0) * 23, heart_y(0) * 23)
    turtle.pendown()  # Abaixa a caneta para começar a desenhar

    for t in range(618):
        x = heart_x(t / 100) * 23
        y = heart_y(t / 100) * 23
        turtle.goto(x, y)

    turtle.hideturtle()  # Esconde a tartaruga após desenhar

if __name__ == "__main__":
    turtle.setup(width=800, height=600)  # Configura o tamanho da janela
    draw_heart()
    turtle.done()  # Mantém a janela aberta após o desenho