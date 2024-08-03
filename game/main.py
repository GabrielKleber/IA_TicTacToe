import tkinter
from tkinter import *
from tkinter import ttk

# Cores

fundo = "#172A3A"
fundoJogadores = "#0C1B33"
corX = "#ff0000"
corO = "#0000ff"
branco = "#fff"


# Janela
janela =  Tk()
janela.title('Jogo da Velha')
janela.geometry('500x610')
janela.configure(bg=fundo)
janela.resizable(False, False)


# Frames da janela
frame_topo = Frame(janela, width=480, height=110, bg=fundoJogadores, relief="raised")
frame_topo.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=480, height=500, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW, padx=10)


# Configurando o frame do topo
app_x = Label(frame_topo, text="X", height=1, relief="flat", anchor="center", font=("Ivy 55 bold"), bg=fundoJogadores, fg=corX)
app_x.place(x=25, y=10)
app_x_jogador = Label(frame_topo, text="Jogador 1", height=1, relief="flat", anchor="center", font=("Ivy 10 bold"), bg=fundoJogadores, fg=branco)
app_x_jogador.place(x=17, y=85)
app_x_pontos = Label(frame_topo, text="0", height=1, relief="flat", anchor="center", font=("Ivy 50 bold"), bg=fundoJogadores, fg=branco)
app_x_pontos.place(x=160, y=15)

app_vs = Label(frame_topo, text=":", height=1, relief="flat", anchor="center", font=("Ivy 45 bold"), bg=fundoJogadores, fg=branco)
app_vs.place(x=228, y=15)

app_o = Label(frame_topo, text="O", height=1, relief="flat", anchor="center", font=("Ivy 55 bold"), bg=fundoJogadores, fg=corO)
app_o.place(x=408, y=10)
app_o_jogador = Label(frame_topo, text="Jogador 2", height=1, relief="flat", anchor="center", font=("Ivy 10 bold"), bg=fundoJogadores, fg=branco)
app_o_jogador.place(x=403, y=85)
app_o_pontos = Label(frame_topo, text="0", height=1, relief="flat", anchor="center", font=("Ivy 50 bold"), bg=fundoJogadores, fg=branco)
app_o_pontos.place(x=285, y=15)



# Criando Lógica do app

jogador_1 = "X"
Jogador_2 = "O"

jogador_1_pontos = 0
jogador_2_pontos = 0

tabela = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

jogando = 'X'
contador = 0
jogar = ''

def iniciar_jogo():
    # Controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        # Comparando o valor recebido
        if i == str(1):
            # verificando se a casa está vazia
            if btn_0_0['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_0_0['fg'] = cor
                btn_0_0['text'] = jogando
                tabela [0][0] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                

        elif i == str(2):
            # verificando se a casa está vazia
            if btn_0_1['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_0_1['fg'] = cor
                btn_0_1['text'] = jogando
                tabela [0][1] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(3):
            # verificando se a casa está vazia
            if btn_0_2['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_0_2['fg'] = cor
                btn_0_2['text'] = jogando
                tabela [0][2] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(4):
            # verificando se a casa está vazia
            if btn_1_0['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_1_0['fg'] = cor
                btn_1_0['text'] = jogando
                tabela [1][0] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(5):
            # verificando se a casa está vazia
            if btn_1_1['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_1_1['fg'] = cor
                btn_1_1['text'] = jogando
                tabela [1][1] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(6):
            # verificando se a casa está vazia
            if btn_1_2['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_1_2['fg'] = cor
                btn_1_2['text'] = jogando
                tabela [1][2] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(7):
            # verificando se a casa está vazia
            if btn_2_0['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_2_0['fg'] = cor
                btn_2_0['text'] = jogando
                tabela [2][0] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(8):
            # verificando se a casa está vazia
            if btn_2_1['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_2_1['fg'] = cor
                btn_2_1['text'] = jogando
                tabela [2][1] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


        elif i == str(9):
            # verificando se a casa está vazia
            if btn_2_2['text'] == '':
                # Verificando o jogador
                if jogando == 'X':
                    cor = corX
                if jogando == 'O':
                    cor = corO

                # Propriedades do Btn
                btn_2_2['fg'] = cor
                btn_2_2['text'] = jogando
                tabela [2][2] = jogando

                # Teste
                ganhou()

                # Verificando quem está jogando
                if jogando == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"


    # Teste
    def ganhou():
        global contador

        contador += 1

        # Verificando se alguém ganhou
        if contador >= 4:
            # linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                vencedor(jogando)

            # colunas
            elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                vencedor(jogando)

            # diagonais
            elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                vencedor(jogando)

            # empate
            elif contador>=9:
                vencedor("empate")

    # Vencedor
    def vencedor(vencedor):
        global tabela
        global contador
        global jogando
        global jogador_1_pontos
        global jogador_2_pontos

        # Bloqueando os botões
        btn_0_0['state'] = 'disable'
        btn_0_1['state'] = 'disable'
        btn_0_2['state'] = 'disable'
        btn_1_0['state'] = 'disable'
        btn_1_1['state'] = 'disable'
        btn_1_2['state'] = 'disable'
        btn_2_0['state'] = 'disable'
        btn_2_1['state'] = 'disable'
        btn_2_2['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text="", width=17, relief="flat", anchor="center", font=("Ivy 20 bold"), bg=fundoJogadores, fg=branco)
        app_vencedor.place(x=100, y=220)

        if vencedor == 'X':
            jogador_1_pontos += 1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_x_pontos['text'] = jogador_1_pontos

        elif vencedor == 'O':
            jogador_2_pontos += 1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_o_pontos['text'] = jogador_2_pontos

        elif vencedor == 'empate':
            app_vencedor['text'] = 'Empate'
            
        def start():
            btn_0_0['text'] = ''
            btn_0_1['text'] = ''
            btn_0_2['text'] = ''
            btn_1_0['text'] = ''
            btn_1_1['text'] = ''
            btn_1_2['text'] = ''
            btn_2_0['text'] = ''
            btn_2_1['text'] = ''
            btn_2_2['text'] = ''

            app_vencedor.destroy()
            btn_jogar.destroy()

            btn_0_0['state'] = 'normal'
            btn_0_1['state'] = 'normal'
            btn_0_2['state'] = 'normal'
            btn_1_0['state'] = 'normal'
            btn_1_1['state'] = 'normal'
            btn_1_2['state'] = 'normal'
            btn_2_0['state'] = 'normal'
            btn_2_1['state'] = 'normal'
            btn_2_2['state'] = 'normal'

        btn_jogar = Button(frame_baixo, command=lambda:start(), text="Proxima Rodada", font=("Ivy 10 bold"), overrelief=RIDGE, relief="flat", bg=fundoJogadores, fg=branco)
        btn_jogar.place(x=185, y=300)

        tabela = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

        contador = 0

        def fimDoJogo():
            btn_jogar.destroy()
            app_vencedor.destroy()

            terminar()

    # Fim do jogo atual
    def terminar():
        global tabela
        global contador
        global jogador_1_pontos
        global jogador_2_pontos
        global contador

        tabela = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

        jogador_1_pontos = 0
        jogador_2_pontos = 0

        btn_0_0['state'] = 'disable'
        btn_0_1['state'] = 'disable'
        btn_0_2['state'] = 'disable'
        btn_1_0['state'] = 'disable'
        btn_1_1['state'] = 'disable'
        btn_1_2['state'] = 'disable'
        btn_2_0['state'] = 'disable'
        btn_2_1['state'] = 'disable'
        btn_2_2['state'] = 'disable'

        def jogar_denovo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'

            btn_jogar.destroy()

            iniciar_jogo()

        # Btn jogar de novo
        btn_jogar = Button(frame_baixo, command=jogar_denovo(), text="Jogar", font=("Ivy 10 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
        btn_jogar.place(x=85, y=197)


    # Configurando o frame de baixo

    # Linhas verticais
    app_v = Label(frame_baixo, text="", height=23, relief="flat", pady=5, anchor="center", font=("Ivy 10 bold"), bg=branco)
    app_v.place(x=177, y=28)
    app_v = Label(frame_baixo, text="", height=23, relief="flat", pady=5, anchor="center", font=("Ivy 10 bold"), bg=branco)
    app_v.place(x=304, y=28)

    # Linhas horizontais
    app_h = Label(frame_baixo, text="", width=365, relief="flat", padx=2, anchor="center", font=("Ivy 1 bold"), bg=branco)
    app_h.place(x=57, y=150)
    app_h = Label(frame_baixo, text="", width=365, relief="flat", padx=2, anchor="center", font=("Ivy 1 bold"), bg=branco)
    app_h.place(x=57, y=279)

    # Btns linha 0
    btn_0_0 = Button(frame_baixo, command=lambda:controlar('1'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_0_0.place(x=57, y=27)

    btn_0_1 = Button(frame_baixo, command=lambda:controlar('2'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_0_1.place(x=183, y=27)

    btn_0_2 = Button(frame_baixo, command=lambda:controlar('3'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_0_2.place(x=310, y=27)

    # Btns linha 1
    btn_1_0 = Button(frame_baixo, command=lambda:controlar('4'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_1_0.place(x=57, y=158)

    btn_1_1 = Button(frame_baixo, command=lambda:controlar('5'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_1_1.place(x=183, y=158)

    btn_1_2 = Button(frame_baixo, command=lambda:controlar('6'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_1_2.place(x=310, y=158)

    # Btns linha 2
    btn_2_0 = Button(frame_baixo, command=lambda:controlar('7'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_2_0.place(x=57, y=287)

    btn_2_1 = Button(frame_baixo, command=lambda:controlar('8'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_2_1.place(x=183, y=287)

    btn_2_2 = Button(frame_baixo, command=lambda:controlar('9'), text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
    btn_2_2.place(x=310, y=287)


iniciar_jogo()

janela.mainloop()

# Vídeo usado como base: https://youtu.be/8qqeHip4NZQ?si=iTEzdmpLj4lpgPjn