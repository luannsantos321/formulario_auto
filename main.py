from customtkinter import *
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Formulário Automatizado")
#win.configure(bg='white')


#Frames
fr = tk.Frame(win, height=100, width=100,bg='white',borderwidth=0.5,relief=tk.SOLID)
fr2 = tk.Frame(win, bg="white", height=100, width=100,borderwidth=0.5,relief=tk.SOLID)
fr3 = tk.Frame(win, bg="white", height=100, width=100,borderwidth=0.5,relief=tk.SOLID)
fr4 = tk.Frame(win, bg="white", height=100, width=100,borderwidth=0.5,relief=tk.SOLID)
fr5 = tk.Frame(win, bg="white", height=100, width=100,borderwidth=0.5,relief=tk.SOLID)




fr.grid(row=0,column=0, padx=5, pady=5)
fr2.grid(row=0,column=4,padx=1, pady=1)
fr3.grid(row=2,column=1,padx=1, pady=1)
fr4.grid(row=3,column=0,padx=1, pady=1)
fr5.grid(row=3,column=2,padx=1, pady=1)

#Combobox
'''lb1 = tk.Label(fr, text="Aparelhos")
aparelho = ttk.Combobox(fr, values='')

lb2 = tk.Label(fr2, text="Modelo")
modelo = ttk.Combobox(fr2, values='')

lb3 = tk.Label(fr3, text="Defeito")
defeito = ttk.Combobox(fr3, values='')

lb4 = tk.Label(fr4, text="Conserto")
conserto = ttk.Combobox(fr4, values='')

lb5 = tk.Label(fr5, text="Destino")
destino = ttk.Combobox(fr5, values='')

lb1.grid(row=0, column=0)
aparelho.grid(row=0, column=0)
lb2.grid(row=0, column=0)
modelo.grid(row=1, column=0)
lb3.grid()
defeito.grid(row=0, column=0)
lb4.grid()
conserto.grid(row=1, column=0)
lb5.grid(row=0, column=0)
destino.grid(row=1, column=0)'''

#Botão
bt = tk.Button(win, text="Clique aqui")

bt.grid(row=4,columnspan=3,sticky='ews')

win.geometry('450x400')
win.mainloop()
