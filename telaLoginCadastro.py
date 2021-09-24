#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 15, 2021 05:26:39 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.top = tk.Tk()
        self.top.geometry("600x450+380+106")
        self.top.minsize(120, 1)
        self.top.maxsize(1364, 749)
        self.top.resizable(1,  1)
        self.top.title("New Toplevel")
        self.top.configure(background="#ffcbdb")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.133, rely=0.156, relheight=0.611
                , relwidth=0.708)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.381, rely=0.036, height=48, width=90)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''LOGIN''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.2, rely=0.4, height=30, relwidth=0.574)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1, show='*')
        self.Entry2.place(relx=0.2, rely=0.655, height=30, relwidth=0.574)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.188, rely=0.291, height=24, width=71)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''USUÁRIO''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.165, rely=0.545, height=21, width=71)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''SENHA''')

        self.button = tk.Button(self.Frame1, command=self.loginBackEnd)
        self.button.place(relx=0.212, rely=0.8, height=34, width=97)
        self.button.configure(activebackground="#ececec")
        self.button.configure(activeforeground="#000000")
        self.button.configure(background="#d9d9d9")
        self.button.configure(disabledforeground="#a3a3a3")
        self.button.configure(foreground="#000000")
        self.button.configure(highlightbackground="#d9d9d9")
        self.button.configure(highlightcolor="black")
        self.button.configure(pady="0")
        self.button.configure(text=''' LOGAR ''')

        self.button_1 = tk.Button(self.Frame1, command=self.cadastro)
        self.button_1.place(relx=0.541, rely=0.8, height=34, width=97)
        self.button_1.configure(activebackground="#ececec")
        self.button_1.configure(activeforeground="#000000")
        self.button_1.configure(background="#d9d9d9")
        self.button_1.configure(disabledforeground="#a3a3a3")
        self.button_1.configure(foreground="#000000")
        self.button_1.configure(highlightbackground="#d9d9d9")
        self.button_1.configure(highlightcolor="black")
        self.button_1.configure(pady="0")
        self.button_1.configure(text='''CADASTRAR''')
        self.top.mainloop()


        
    def cadastro(self):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'

            self.root = tk.Tk()
            self.root.geometry("600x450+380+106")
            self.root.minsize(120, 1)
            self.root.maxsize(1364, 749)
            self.root.resizable(1, 1)
            self.root.title("Cadastro")
            #self.root.configure(background="#d9d9d9")
            self.root.configure(background="#add8e6")

            self.frameCadastro = tk.Frame(self.root)
            self.frameCadastro.place(relx=0.133, rely=0.156, relheight=0.611
                                     , relwidth=0.708)
            self.frameCadastro.configure(relief='groove')
            self.frameCadastro.configure(borderwidth="2")
            self.frameCadastro.configure(relief="groove")
            self.frameCadastro.configure(background="#d9d9d9")

            self.Label1Cadastro = tk.Label(self.frameCadastro)
            self.Label1Cadastro.place(relx=0.381, rely=0.036, height=48, width=90)
            self.Label1Cadastro.configure(background="#d9d9d9")
            self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
            self.Label1Cadastro.configure(foreground="#000000")
            self.Label1Cadastro.configure(text='''CADASTRO''')

            self.Entry1Cadastro = tk.Entry(self.frameCadastro)
            self.Entry1Cadastro.place(relx=0.2, rely=0.4, height=30, relwidth=0.574)
            self.Entry1Cadastro.configure(background="white")
            self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
            self.Entry1Cadastro.configure(font="TkFixedFont")
            self.Entry1Cadastro.configure(foreground="#000000")
            self.Entry1Cadastro.configure(insertbackground="black")

            self.Entry2Cadastro = tk.Entry(self.frameCadastro, show='*')
            self.Entry2Cadastro.place(relx=0.2, rely=0.655, height=30, relwidth=0.574)
            self.Entry2Cadastro.configure(background="white")
            self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
            self.Entry2Cadastro.configure(font="TkFixedFont")
            self.Entry2Cadastro.configure(foreground="#000000")
            self.Entry2Cadastro.configure(insertbackground="black")

            self.Label2Cadastro = tk.Label(self.frameCadastro)
            self.Label2Cadastro.place(relx=0.188, rely=0.291, height=24, width=71)
            self.Label2Cadastro.configure(background="#d9d9d9")
            self.Label2Cadastro.configure(disabledforeground="#a3a3a3")
            self.Label2Cadastro.configure(foreground="#000000")
            self.Label2Cadastro.configure(text='''USUÁRIO''')

            self.Label2Cadastro_1 = tk.Label(self.frameCadastro)
            self.Label2Cadastro_1.place(relx=0.165, rely=0.545, height=21, width=71)
            self.Label2Cadastro_1.configure(activebackground="#f9f9f9")
            self.Label2Cadastro_1.configure(activeforeground="black")
            self.Label2Cadastro_1.configure(background="#d9d9d9")
            self.Label2Cadastro_1.configure(disabledforeground="#a3a3a3")
            self.Label2Cadastro_1.configure(foreground="#000000")
            self.Label2Cadastro_1.configure(highlightbackground="#d9d9d9")
            self.Label2Cadastro_1.configure(highlightcolor="black")
            self.Label2Cadastro_1.configure(text='''SENHA''')

            self.button1Cadastro_3 = tk.Button(self.frameCadastro, command=self.cadastrarBackEnd)
            self.button1Cadastro_3.place(relx=0.541, rely=0.8, height=34, width=97)
            self.button1Cadastro_3.configure(activebackground="#ececec")
            self.button1Cadastro_3.configure(activeforeground="#000000")
            self.button1Cadastro_3.configure(background="#d9d9d9")
            self.button1Cadastro_3.configure(disabledforeground="#a3a3a3")
            self.button1Cadastro_3.configure(foreground="#000000")
            self.button1Cadastro_3.configure(highlightbackground="#d9d9d9")
            self.button1Cadastro_3.configure(highlightcolor="black")
            self.button1Cadastro_3.configure(pady="0")
            self.button1Cadastro_3.configure(text='''CADASTRAR''')
            self.root.mainloop()

    def cadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')

            with open('senhas.txt', 'a') as arquivoSenha:
                arquivoSenha.write(self.Entry2Cadastro.get() + '\n')
            self.root.destroy()
        except:
            print('Houve um erro')

    def loginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        with open('senhas.txt', 'r') as arquivoSenha:
            senhas = arquivoSenha.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''), usuarios))

        senhas = list(map(lambda x: x.replace('\n', ''), senhas))

        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False
        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('usuario logado')
                logado = True
                self.top.destroy()

        if not logado:
            print('dados incorretos')
            self.top.destroy()



Toplevel1()

