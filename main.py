import tkinter as tk
from tkinter import ttk
import turtle

def desenhar_forma():
    t.clear()
    t.penup()
    t.goto(0, -50)  # centraliza o desenho
    t.pendown()
    t.fillcolor(cor_escolhida.get())
    t.begin_fill()

    forma = forma_escolhida.get()

    if forma == "Triângulo":
        for _ in range(3):
            t.forward(100)
            t.left(120)
    elif forma == "Quadrado":
        for _ in range(4):
            t.forward(100)
            t.left(90)
    elif forma == "Círculo":
        t.circle(50)

    t.end_fill()

def limpar_desenho():
    t.clear()

def pre_visualizar():
    canvas_preview.delete("all")
    cor = cor_escolhida.get()

    if forma_escolhida.get() == "Triângulo":
        canvas_preview.create_polygon(75, 20, 20, 130, 130, 130, fill=cor, outline="black")
    elif forma_escolhida.get() == "Quadrado":
        canvas_preview.create_rectangle(40, 40, 120, 120, fill=cor, outline="black")
    elif forma_escolhida.get() == "Círculo":
        canvas_preview.create_oval(40, 40, 120, 120, fill=cor, outline="black")

janela = tk.Tk()
janela.title("Desenho Interativo")
janela.geometry("600x700")

forma_escolhida = tk.StringVar(value="Triângulo")
cor_escolhida = tk.StringVar(value="blue")

frame_principal = ttk.Frame(janela)
frame_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

label_instrucao = ttk.Label(frame_principal, text="Escolha uma forma e uma cor:", font=("Arial", 14))
label_instrucao.pack(pady=10)
label_instrucao.pack_configure(anchor="center")

# Frame superior para seleção e pré-visualização lado a lado, centralizado
frame_superior = ttk.Frame(frame_principal)
frame_superior.pack(pady=10)
frame_superior.pack_configure(anchor="center")

frame_formas = ttk.LabelFrame(frame_superior, text="Formas")
frame_formas.pack(side=tk.LEFT, padx=20)
frame_formas.pack_configure(anchor="center")

formas = ["Triângulo", "Quadrado", "Círculo"]
for forma in formas:
    ttk.Radiobutton(frame_formas, text=forma, variable=forma_escolhida, value=forma).pack(anchor="w")

frame_cores = ttk.LabelFrame(frame_superior, text="Cores")
frame_cores.pack(side=tk.LEFT, padx=20)
frame_cores.pack_configure(anchor="center")

cores = [("Azul", "blue"), ("Vermelho", "red"), ("Amarelo", "yellow")]
for nome, valor in cores:
    ttk.Radiobutton(frame_cores, text=nome, variable=cor_escolhida, value=valor).pack(anchor="w")

canvas_preview = tk.Canvas(frame_superior, width=150, height=150, bg="white")
canvas_preview.pack(side=tk.LEFT, padx=20)

# Frame para área de desenho Turtle, abaixo da seleção/pré-visualização, centralizado
frame_desenho = ttk.Frame(frame_principal)
frame_desenho.pack(pady=20)
frame_desenho.pack_configure(anchor="center")

canvas_turtle = tk.Canvas(frame_desenho, width=400, height=400)
canvas_turtle.pack()

screen = turtle.TurtleScreen(canvas_turtle)
screen.bgcolor("white")

t = turtle.RawTurtle(screen)
t.speed(3)

# Frame dos botões, abaixo do desenho, centralizado
frame_botoes = ttk.Frame(frame_principal)
frame_botoes.pack(pady=10)
frame_botoes.pack_configure(anchor="center")

btn_prever = ttk.Button(frame_botoes, text="Pré-visualizar", command=pre_visualizar)
btn_prever.grid(row=0, column=0, padx=10)

btn_desenhar = ttk.Button(frame_botoes, text="Desenhar", command=desenhar_forma)
btn_desenhar.grid(row=0, column=1, padx=10)

btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_desenho)
btn_limpar.grid(row=0, column=2, padx=10)

janela.mainloop()