import customtkinter
import tkinter as tk
from tkinter import ttk





win = tk.Tk()
win.title("Formulário Automatizado")
win.configure(bg='white')

#Aparelhos
lb_aparelho = tk.LabelFrame(win,text='Aparelhos',bg='white',fg='orange'
                            , padx=10, pady=10,font='Verdana, 30')
aparelho = ttk.Combobox(lb_aparelho)

lb_aparelho.place(x=40,y=90)
aparelho.pack()

#modelos
#
#(x=55,y=110)
lb_modelo = tk.LabelFrame(win,text='Modelos',bg='white',fg='orange'
                            , padx=10, pady=10)
modelo = ttk.Combobox(lb_modelo)

lb_modelo.place(x=250,y=90)
modelo.pack()

#defeito
lb_defeito = tk.LabelFrame(win,text='Defeito',bg='white',fg='orange'
                            , padx=10, pady=10)
defeito = ttk.Combobox(lb_defeito)

lb_defeito.place(x=40,y=180)
defeito.pack()

#conserto
lb_conserto = tk.LabelFrame(win,text='Conserto',bg='white',fg='orange'
                            , padx=10, pady=10)
conserto = ttk.Combobox(lb_conserto)

lb_conserto.place(x=250,y=180)
conserto.pack()

#Destino
lb_destino =tk.LabelFrame(win,text='Destino',bg='white',fg='orange'
                            , padx=10, pady=10)
destino = ttk.Combobox(lb_destino)

lb_destino.place(x=140,y=250)
destino.pack()

#botão
bt = customtkinter.CTkButton(text='GO!', width=450, corner_radius=0, 
                             fg_color='orange',text_color='white')
bt.pack(side='bottom')
win.maxsize(450,450)
win.geometry('450x450')
win.mainloop()

