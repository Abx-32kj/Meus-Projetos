#Calculadora do ROCK oficialmente pronta !!!!!!!

from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Calculadora do ROCK")
janela.geometry("305x413")
janela.config(bg="#3b3b3b")

# Criando o corpo da calculadora
frame_tela = Frame(janela, width=350, height=80, bg="#394161")
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=400)
frame_corpo.grid(row=1, column=0)

#Criando a lógica da minha calculadora do ROCK

    # Variável todos_valores para armazenar os valores digitados

todos_valores = ""

valor_texto = StringVar()

def entrar_valores(evento):

    global todos_valores

    todos_valores = todos_valores + str(evento)

    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set(todos_valores)    


# Agora vamos criar a tela da calculadora do ROCK

app_tela = Label(frame_tela, textvariable= valor_texto, width=17, height=3, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Arial", 21, "bold"), bg= "#394161", fg="white")
app_tela.place(x=0, y=0)

# Agora vamos criar os botões dessa calcuadora do ROCK

#Botões da primeira linha... do ROCK
b1 = Button(frame_corpo, text="C", width=11, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command= limpar_tela)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text="%", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('%'))
b2.place(x=155, y=0)

b3 = Button(frame_corpo, text="/", width=5, height=2, bg="#FF8026", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, fg="white", command=lambda: entrar_valores('/'))
b3.place(x=230, y=0)

#Botões da segunda linha... do ROCK

b4 = Button(frame_corpo, text="7", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('7'))
b4.place(x=1, y=67)

b5 = Button(frame_corpo, text="8", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('8'))
b5.place(x=78, y=67)

b6 = Button(frame_corpo, text="9", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('9'))
b6.place(x=155, y=67)

b8 = Button(frame_corpo, text="*", width=5, height=2, bg="#FF8026", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, fg="white", command=lambda: entrar_valores('*'))
b8.place(x=230, y=67)

#Botões da terceira linha... do ROCK

b9 = Button(frame_corpo, text="4", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('4'))
b9.place(x=1, y=134)

b10 = Button(frame_corpo, text="5", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('5'))
b10.place(x=78, y=134)

b11 = Button(frame_corpo, text="6", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('6'))
b11.place(x=155, y=134)

b12 = Button(frame_corpo, text="-", width=5, height=2, bg="#FF8026", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, fg="white", command=lambda: entrar_valores('-'))
b12.place(x=230, y=134)

#Botões da terceira linha... do ROCK

b13 = Button(frame_corpo, text="1", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('1'))
b13.place(x=1, y=201)

b14 = Button(frame_corpo, text="2", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('2'))
b14.place(x=78, y=201)

b15 = Button(frame_corpo, text="3", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('3'))
b15.place(x=155, y=201)

b16 = Button(frame_corpo, text="+", width=5, height=2, bg="#FF8026", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, fg="white", command=lambda: entrar_valores('+'))
b16.place(x=230, y=201)

#Botões da ultima linha... do ROCK

b17 = Button(frame_corpo, text="0", width=11, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('0'))
b17.place(x=1, y=268)

b18 = Button(frame_corpo, text=".", width=5, height=2, bg="#BCBCBC", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('.'))
b18.place(x=155, y=268)

b19 = Button(frame_corpo, text="=", width=5, height=2, bg="#FF8026", font=("Arial", 16, "bold"), relief=RAISED, overrelief=RIDGE, fg="white", command= calcular)
b19.place(x=230, y=268)

janela.mainloop()