import tkinter as tk
import locale
from time import strftime

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

janela = tk.Tk()
janela.title("Relógio Digital de Arthur")
janela.geometry("450x300")
janela.configure(bg="White")

data_label = tk.Label(janela, font=("Arial", 15), background="White", foreground="Black")
data_label.pack(pady=5)

relogio = tk.Label(janela, font=("Arial", 40), background="White", foreground="Black")
relogio.pack(expand="true") 

def atualizar():
    hora = strftime("%H:%M:%S")  
    data = strftime("%A /%d de %B de %Y")
    relogio.config(text=hora)
    data_label.config(text=data.capitalize())
    relogio.after(1000, atualizar)  

atualizar()
janela.mainloop()