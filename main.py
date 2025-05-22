import turtle


screen = turtle.Screen() 
screen.setup(width=800, height=600) 
screen.title("Programa de Desenho Interativo com Turtle") 
screen.bgcolor("lightgray") 

pen = turtle.Turtle() 
pen.speed(3)
pen.penup()
pen.goto(0, 0)
pen.pendown() 
pen.hideturtle() 

def draw_square(size, color):
    pen.clear()
    pen.penup()
    pen.goto(-size / 2, size / 2)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def draw_triangle(size, color):
    pen.clear()
    pen.penup()
    pen.goto(-size / 2, -size * (3**0.5) / 6)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def draw_circle(radius, color):
    pen.clear()
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def get_shape_choice():
    while True:
        try:
            choice = int(screen.textinput("Seleção de Forma",
                                         "Selecione uma forma:\n1 para Quadrado\n2 para Triângulo\n3 para Círculo"))
            if choice in [1, 2, 3]:
                return choice
            else:
                screen.textinput("Erro", "Opção inválida. Por favor, digite 1, 2 ou 3.")
        except (ValueError, TypeError):
            screen.textinput("Erro", "Entrada inválida. Por favor, digite um número.")

def get_color_choice():
    color_map = {
        "vermelho": "red", "red": "red",
        "azul": "blue", "blue": "blue",
        "verde": "green", "green": "green",
        "amarelo": "yellow", "yellow": "yellow",
        "roxo": "purple", "purple": "purple",
        "laranja": "orange", "orange": "orange"
    }

    while True:
        color_name_input = screen.textinput("Seleção de Cor",
                                            "Escolha uma cor (vermelho, azul, verde, amarelo, roxo, laranja):").lower()

        if color_name_input in color_map:
            return color_map[color_name_input]
        else:
            screen.textinput("Erro", "Cor inválida. Escolha entre vermelho, azul, verde, amarelo, roxo, laranja.")

def main_loop():
    pen.pencolor("black")
    pen.pensize(2)

    while True:
        shape_choice = get_shape_choice()
        color_choice = get_color_choice()

        if shape_choice == 1:
            draw_square(150, color_choice)
        elif shape_choice == 2:
            draw_triangle(180, color_choice)
        elif shape_choice == 3:
            draw_circle(75, color_choice)
        else:
            screen.textinput("Erro Fatal", "Uma escolha de forma inesperada ocorreu.")

        continue_drawing = screen.textinput("Desenho Concluído!",
                                            "Desenho concluído! Deseja fazer outro desenho?\nDigite 'sim' para continuar ou qualquer outra coisa para sair.").lower()

        if continue_drawing != 'sim':
            break


if __name__ == "__main__":
    main_loop()
    screen.textinput("Saindo", "Obrigado por usar o programa de desenho! Pressione OK para fechar.")
    screen.bye()