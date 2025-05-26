# Importa as bibliotecas necessárias:
# tkinter para a interface gráfica do usuário (GUI)
import tkinter as tk
# ttk para widgets temáticos do tkinter (melhor aparência)
from tkinter import ttk
# turtle para desenhar gráficos vetoriais (formas)
import turtle

# Função para desenhar a forma selecionada no canvas do Turtle
def desenhar_forma():
    # Limpa qualquer desenho anterior no canvas do Turtle
    t.clear()
    # Levanta a caneta para mover o cursor do Turtle sem desenhar
    t.penup()
    # Move o cursor do Turtle para uma posição inicial (para centralizar o desenho)
    t.goto(0, -50)
    # Abaixa a caneta para começar a desenhar
    t.pendown()
    # Define a cor de preenchimento da forma com base na cor escolhida na interface
    t.fillcolor(cor_escolhida.get())
    # Inicia o processo de preenchimento da forma
    t.begin_fill()

    # Obtém a forma selecionada pelo usuário na interface
    forma = forma_escolhida.get()

    # Verifica qual forma foi selecionada e a desenha
    if forma == "Triângulo":
        # Desenha um triângulo equilátero
        for _ in range(3):  # Repete 3 vezes (para os 3 lados)
            t.forward(100)  # Move para frente 100 unidades
            t.left(120)     # Vira 120 graus para a esquerda
    elif forma == "Quadrado":
        # Desenha um quadrado
        for _ in range(4):  # Repete 4 vezes (para os 4 lados)
            t.forward(100)  # Move para frente 100 unidades
            t.left(90)      # Vira 90 graus para a esquerda
    elif forma == "Círculo":
        # Desenha um círculo com raio de 50 unidades
        t.circle(50)

    # Finaliza o processo de preenchimento da forma
    t.end_fill()

# Função para limpar o desenho no canvas do Turtle
def limpar_desenho():
    # Limpa completamente o canvas do Turtle
    t.clear()

# Função para pré-visualizar a forma e a cor selecionadas no canvas de pré-visualização
def pre_visualizar():
    # Limpa qualquer desenho anterior no canvas de pré-visualização
    canvas_preview.delete("all")
    # Obtém a cor selecionada pelo usuário
    cor = cor_escolhida.get()

    # Verifica qual forma foi selecionada e desenha uma miniatura no canvas de pré-visualização
    if forma_escolhida.get() == "Triângulo":
        # Desenha um polígono (triângulo) no canvas de pré-visualização
        # Coordenadas: (x1, y1, x2, y2, x3, y3, ...)
        canvas_preview.create_polygon(75, 20, 20, 130, 130, 130, fill=cor, outline="black")
    elif forma_escolhida.get() == "Quadrado":
        # Desenha um retângulo (quadrado) no canvas de pré-visualização
        # Coordenadas: (x_superior_esquerdo, y_superior_esquerdo, x_inferior_direito, y_inferior_direito)
        canvas_preview.create_rectangle(40, 40, 120, 120, fill=cor, outline="black")
    elif forma_escolhida.get() == "Círculo":
        # Desenha uma oval (círculo) no canvas de pré-visualização
        # Coordenadas da caixa delimitadora: (x_superior_esquerdo, y_superior_esquerdo, x_inferior_direito, y_inferior_direito)
        canvas_preview.create_oval(40, 40, 120, 120, fill=cor, outline="black")

# --- Configuração da Janela Principal ---
# Cria a janela principal da aplicação
janela = tk.Tk()
# Define o título da janela
janela.title("Desenho Interativo")
# Define as dimensões iniciais da janela (largura x altura)
janela.geometry("600x700")

# --- Variáveis de Controle do Tkinter ---
# StringVar para armazenar a forma atualmente selecionada (valor inicial: "Triângulo")
forma_escolhida = tk.StringVar(value="Triângulo")
# StringVar para armazenar a cor atualmente selecionada (valor inicial: "blue")
cor_escolhida = tk.StringVar(value="blue")

# --- Estrutura de Layout com Frames ---
# Cria um frame principal para organizar todos os outros widgets
frame_principal = ttk.Frame(janela)
# Empacota o frame principal na janela, permitindo que ele se expanda e preencha o espaço
# padx e pady adicionam um preenchimento (espaçamento) ao redor do frame
frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Cria um rótulo de instrução
label_instrucao = ttk.Label(frame_principal, text="Escolha uma forma e uma cor:", font=("Arial", 14))
# Empacota o rótulo no frame principal com um preenchimento vertical
label_instrucao.pack(pady=10)
# Configura o rótulo para ser centralizado horizontalmente
label_instrucao.pack_configure(anchor="center")

# Frame superior para agrupar seleção de formas, cores e a pré-visualização
frame_superior = ttk.Frame(frame_principal)
# Empacota o frame superior no frame principal
frame_superior.pack(pady=10)
# Configura o frame superior para ser centralizado horizontalmente
frame_superior.pack_configure(anchor="center")

# Frame para os botões de seleção de forma (Radiobuttons)
frame_formas = ttk.LabelFrame(frame_superior, text="Formas")
# Empacota o frame de formas à esquerda dentro do frame superior, com preenchimento horizontal
frame_formas.pack(side=tk.LEFT, padx=20)
# Configura o frame de formas para ser centralizado (relativo ao seu espaço no 'side=tk.LEFT')
frame_formas.pack_configure(anchor="center")

# Lista de formas disponíveis
formas = ["Triângulo", "Quadrado", "Círculo"]
# Cria um Radiobutton para cada forma na lista
for forma in formas:
    # Cada Radiobutton está associado à variável 'forma_escolhida'
    # 'value=forma' define o valor que 'forma_escolhida' terá quando este botão for selecionado
    # 'anchor="w"' alinha o texto do botão à esquerda (West)
    ttk.Radiobutton(frame_formas, text=forma, variable=forma_escolhida, value=forma).pack(anchor="w")

# Frame para os botões de seleção de cor (Radiobuttons)
frame_cores = ttk.LabelFrame(frame_superior, text="Cores")
# Empacota o frame de cores à esquerda dentro do frame superior, com preenchimento horizontal
frame_cores.pack(side=tk.LEFT, padx=20)
# Configura o frame de cores para ser centralizado
frame_cores.pack_configure(anchor="center")

# Lista de cores disponíveis (nome exibido, valor real da cor)
cores = [("Azul", "blue"), ("Vermelho", "red"), ("Amarelo", "yellow")]
# Cria um Radiobutton para cada cor na lista
for nome, valor in cores:
    # Cada Radiobutton está associado à variável 'cor_escolhida'
    # 'value=valor' define o valor que 'cor_escolhida' terá quando este botão for selecionado
    ttk.Radiobutton(frame_cores, text=nome, variable=cor_escolhida, value=valor).pack(anchor="w")

# Canvas para a pré-visualização da forma e cor
canvas_preview = tk.Canvas(frame_superior, width=150, height=150, bg="white")
# Empacota o canvas de pré-visualização à esquerda dentro do frame superior
canvas_preview.pack(side=tk.LEFT, padx=20)

# Frame para a área de desenho do Turtle
frame_desenho = ttk.Frame(frame_principal)
# Empacota o frame de desenho no frame principal
frame_desenho.pack(pady=20)
# Configura o frame de desenho para ser centralizado
frame_desenho.pack_configure(anchor="center")

# Canvas onde o Turtle irá desenhar
canvas_turtle = tk.Canvas(frame_desenho, width=400, height=400)
# Empacota o canvas do Turtle dentro do frame de desenho
canvas_turtle.pack()

# --- Configuração do Turtle ---
# Cria uma tela do Turtle associada ao canvas_turtle
screen = turtle.TurtleScreen(canvas_turtle)
# Define a cor de fundo da tela do Turtle
screen.bgcolor("white")

# Cria um objeto Turtle (a "caneta") que desenhará na 'screen'
t = turtle.RawTurtle(screen)
# Define a velocidade do desenho do Turtle (1=lento, 10=rápido, 0=mais rápido)
t.speed(3)

# Frame para os botões de ação (Pré-visualizar, Desenhar, Limpar)
frame_botoes = ttk.Frame(frame_principal)
# Empacota o frame de botões no frame principal
frame_botoes.pack(pady=10)
# Configura o frame de botões para ser centralizado
frame_botoes.pack_configure(anchor="center")

# Botão para acionar a função de pré-visualização
btn_prever = ttk.Button(frame_botoes, text="Pré-visualizar", command=pre_visualizar)
# Posiciona o botão na grade (grid) do frame_botoes
btn_prever.grid(row=0, column=0, padx=10)

# Botão para acionar a função de desenhar a forma
btn_desenhar = ttk.Button(frame_botoes, text="Desenhar", command=desenhar_forma)
# Posiciona o botão na grade
btn_desenhar.grid(row=0, column=1, padx=10)

# Botão para acionar a função de limpar o desenho
btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_desenho)
# Posiciona o botão na grade
btn_limpar.grid(row=0, column=2, padx=10)

# Inicia o loop principal da interface gráfica do Tkinter
# Mantém a janela aberta e responsiva aos eventos do usuário
janela.mainloop()