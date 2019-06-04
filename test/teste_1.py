# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Cadastro de Funcionário")
window.geometry('400x400')
window.configure(background = "grey")
a = Label(window, text = "Nome Completo").grid(row = 0, column = 0)
b = Label(window, text = "CPF").grid(row = 1, column = 0)
c = Label(window, text = "RG").grid(row = 2, column = 0)
d = Label(window, text = "Data de Nascimento").grid(row = 3, column = 0)
e = Label(window, text = "Endereço").grid(row = 4, column = 0)
f = Label(window, text = "Cargo").grid(row = 5, column = 0)
g = Label(window, text = "Telefone").grid(row = 6, column = 0)
h = Label(window, text = "Salário Bruto").grid(row = 7, column = 0)

nome = Entry(window).grid(row = 0,column = 1)
cpf = Entry(window).grid(row = 1,column = 1)
rg = Entry(window).grid(row = 2,column = 1)
dataNasc = Entry(window).grid(row = 3,column = 1)
endereco = Entry(window).grid(row = 4,column = 1)
cargo = Entry(window).grid(row = 5,column = 1)
telefone = Entry(window).grid(row = 6,column = 1)
salario_bruto = Entry(window).grid(row = 7,column = 1)

btn = ttk.Button(window, text = "Enviar").grid(row = 9, column = 0)
window.mainloop()
