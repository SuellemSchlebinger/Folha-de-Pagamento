# -*- coding=utf-8 -*-

import tkinter as tk                # python 3
from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont # python 3

class FolhaPgto(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (homepage, confirmacao, relatorio):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("homepage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Cadastro do Funcionário", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        v0 = tk.Label(self, text = "Nome Completo")
        v0.pack(fill="x", padx=10, pady=5)
        self.nome = tk.Entry(self)
        self.nome.pack(fill="x", padx=10, pady=5)

        v1 = tk.Label(self, text="CPF")
        v1.pack(fill="x", padx=10, pady=5)
        self.cpf = tk.Entry(self)
        self.cpf.pack(fill="x", padx=10, pady=5)

        v2 = tk.Label(self, text="RG")
        v2.pack(fill="x", padx=10, pady=5)
        self.rg = tk.Entry(self)
        self.rg.pack(fill="x", padx=10, pady=5)

        v3 = tk.Label(self, text="Data de Nascimento")
        v3.pack(fill="x", padx=10, pady=5)
        self.dataNasc = tk.Entry(self)
        self.dataNasc.pack(fill="x", padx=10, pady=5)

        v4 = tk.Label(self, text="Endereço")
        v4.pack(fill="x", padx=10, pady=5)
        self.endereco = tk.Entry(self)
        self.endereco.pack(fill="x", padx=10, pady=5)

        v5 = tk.Label(self, text="Cargo")
        v5.pack(fill="x", padx=10, pady=5)
        self.cargo = tk.Entry(self)
        self.cargo.pack(fill="x", padx=10, pady=5)

        v6 = tk.Label(self, text="Telefone")
        v6.pack(fill="x", padx=10, pady=5)
        self.telefone = tk.Entry(self)
        self.telefone.pack(fill="x", padx=10, pady=5)

        v7 = tk.Label(self, text="Salário Bruto")
        v7.pack(fill="x", padx=10, pady=5)
        self.salario_bruto = tk.Entry(self)
        self.salario_bruto.pack(fill="x", padx=10, pady=5)

        button1 = tk.Button(self, text="Enviar registro",
                            command=lambda: controller.show_frame("confirmacao"))
        button1.pack(side="bottom", pady=5)

class salario:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def inss1(self):
        sb = self.salario_bruto
        if sb >= 0 and sb <= 1693.72:
            inss = (sb * 0.08)
        if sb >= 1693.73 and sb <= 2822.90:
            inss = (sb * 0.09)
        if sb >= 2822.91 and sb <= 5645.80:
           inss = (sb* 0.11)
        inss = ((inss*100 + 0.5) / 100.0)
        return inss

    def salario_com_contribuicao(self):
        sb = self.salario_bruto
        inss = self.inss1()
        salCon = sb - inss
        return (salCon)
    def irrf1(self):
        atual = self.salario_com_contribuicao()
        if (atual >= 0 and atual < 1903.99):
            irrf = (atual * 0)

        if (atual > 1903.99 and atual < 2826.65):
            irrf = (atual * 0.075) - 142.80

        if (atual > 2826.66 and atual < 3751.05):
            irrf = (atual* 0.15) - 354.80

        if (atual > 3751.06 and atual < 4664.68):
            irrf = (atual * 0.225) - 636.13

        if (atual> 4664.69):
            irrf = (atual * 0.275) - 869.36
        irrf = (irrf * 100 + 0.5) / 100.0
        return irrf
    def salarioliquido(self):
        sb = self.salario_bruto
        inss = self.inss1()
        irrf = self.irrf1()
        saLiq = (sb - inss - irrf)
        return (saLiq)


class confirmacao(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Funcionário cadastrado com sucesso!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Gerar folha de pagamento",
                           command=lambda: controller.show_frame("relatorio"))
        button1.pack()

        button2 = tk.Button(self, text="Sair",
                            command=quit)
        button2.pack()

def valores(self, controller):
    return homepage(self, controller)




class relatorio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Relatório da Folha de Pagamento", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        var = valores(self, controller)

        v0 = tk.Label(self, text="Nome Completo")
        v0.pack(fill="x", padx=10, pady=5)
        nomei = tk.Label(self, var.nome)
        nomei.pack(fill="x", padx=10, pady=5)

        v1 = tk.Label(self, text="CPF")
        v1.pack(fill="x", padx=10, pady=5)
        cpf = tk.Entry(self)
        cpf.pack(fill="x", padx=10, pady=5)

        v2 = tk.Label(self, text="RG")
        v2.pack(fill="x", padx=10, pady=5)
        rg = tk.Entry(self)
        rg.pack(fill="x", padx=10, pady=5)

        v3 = tk.Label(self, text="Data de Nascimento")
        v3.pack(fill="x", padx=10, pady=5)
        dataNasc = tk.Entry(self)
        dataNasc.pack(fill="x", padx=10, pady=5)

        v4 = tk.Label(self, text="Endereço")
        v4.pack(fill="x", padx=10, pady=5)
        endereco = tk.Entry(self)
        endereco.pack(fill="x", padx=10, pady=5)

        v5 = tk.Label(self, text="Cargo")
        v5.pack(fill="x", padx=10, pady=5)
        cargo = tk.Entry(self)
        cargo.pack(fill="x", padx=10, pady=5)

        v6 = tk.Label(self, text="Telefone")
        v6.pack(fill="x", padx=10, pady=5)
        telefone = tk.Entry(self)
        telefone.pack(fill="x", padx=10, pady=5)

        v7 = tk.Label(self, text="Salário Bruto")
        v7.pack(fill="x", padx=10, pady=5)
        salario_bruto = tk.Entry(self)
        salario_bruto.pack(fill="x", padx=10, pady=5)

        button = tk.Button(self, text="Sair",
                           command=quit)
        button.pack()


if __name__ == "__main__":
    app = FolhaPgto()
    app.mainloop()
