from tkinter import *
from tkinter.ttk import *
from math import factorial


def func():
    a = entrada_a.get()
    b = entrada_b.get()
    n = int(entrada_n.get())
    
    if a[-1].isdigit():
        a_inc = 1
    else:
        a_inc = a[-1]
        a = a[:-1]
        
    if b[-1].isdigit():
        b_inc = 1
    else:
        b_inc = b[-1]
        b = b[:-1]
    
    if a == "":
        a = 1
        
    if b == "":
        b = 1
    
    a = int(a)
    b = int(b)
    resp = ""
    
    for p in range(n+1):
        termo = int((factorial(n)/(factorial(p)*factorial(n-p)))*(a**(n-p))*(b**p))
        if p>0:
            print(" ", end="")
            resp = resp + " "
            if termo>0:
                print("+", end="")
                resp = resp + "+"
        print(termo, end="")
        resp = resp + str(termo)
        if a_inc != 1 and n-p>0:
            print(f'.{a_inc}', end="")
            resp = resp + "." + a_inc
            if n-p>1:
                print(f'^{n-p}', end="")
                resp = resp + "^" + str(n-p)
        if b_inc != 1 and p>0:
            print(f'.{b_inc}', end="")
            resp = resp + "." + str(b_inc)
            if p != 1:
                print(f'^{p}')
                resp = resp + "^" + str(p)
    print("")
    resposta.set(resp)
                

master = Tk()
master.title("Binômio de Newton")

largura = 1100
altura = 300
largura_tela = master.winfo_screenwidth()
altura_tela = master.winfo_screenheight()
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

#master.geometry(newGeometry="%dx%d+%d+%d" % (largura, altura, posx, posy))

texto_orientacao = Label(
    master,
    text = "Insira os valores para gerar um polinômio a partir do Binômio de Newton (a+b)^n",
    font = "Arial 20"
    )

texto_1 = Label(
    master,
    text = " (",
    font = "Arial 12",
    #bd = 5,
    relief = "solid",
    )

entrada_a = Entry(
    master,
    font = "Arial 12",
    width = 10
    )

texto_2 = Label(
    master,
    text = "+",
    font = "Arial 12",
    #bd = 5,
    relief = "solid",
    )

entrada_b = Entry(
    master,
    font = "Arial 12",
    width = 10
    )

texto_3 = Label(
    master,
    text = ")^",
    font = "Arial 12",
    #bd = 5,
    relief = "solid",
    )

entrada_n = Entry(
    master,
    font = "Arial 12",
    width = 10
    )

texto_4 = Label(
    master,
    text = "=",
    font = "Arial 12",
    #bd = 5,
    relief = "solid",
    )

resposta = StringVar()
resposta.set("Resposta")

texto_5 = Label(
    master,
    textvariable = resposta,
    font = "Arial 12",
    #bd = 5,
    relief = "solid",
    )

botao = Button(
    master,
    text = "Gerar o polinômio equivalente",
    width = "50",
    #font = "Arial 15",
    command = func
    )

# layout

texto_orientacao.grid(row=0, columnspan=8, padx="20", pady="30")

texto_1.grid(row=1, column=0)

entrada_a.grid(row=1, column=1)

texto_2.grid(row=1, column=2)

entrada_b.grid(row=1, column=3)

texto_3.grid(row=1, column=4)

entrada_n.grid(row=1, column=5)

texto_4.grid(row=1, column=6)

texto_5.grid(row=2, columnspan=8)

botao.grid(row=3, columnspan=8)


master.mainloop()