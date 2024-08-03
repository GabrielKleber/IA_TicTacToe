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
app_x_pontos.place(x=180, y=15)

app_vs = Label(frame_topo, text=":", height=1, relief="flat", anchor="center", font=("Ivy 45 bold"), bg=fundoJogadores, fg=branco)
app_vs.place(x=228, y=15)

app_o = Label(frame_topo, text="O", height=1, relief="flat", anchor="center", font=("Ivy 55 bold"), bg=fundoJogadores, fg=corO)
app_o.place(x=408, y=10)
app_o_jogador = Label(frame_topo, text="Jogador 2", height=1, relief="flat", anchor="center", font=("Ivy 10 bold"), bg=fundoJogadores, fg=branco)
app_o_jogador.place(x=403, y=85)
app_o_pontos = Label(frame_topo, text="0", height=1, relief="flat", anchor="center", font=("Ivy 50 bold"), bg=fundoJogadores, fg=branco)
app_o_pontos.place(x=260, y=15)


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
btn_0_0 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_0_0.place(x=57, y=27)

btn_0_1 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_0_1.place(x=183, y=27)

btn_0_2 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_0_2.place(x=310, y=27)

# Btns linha 1
btn_1_0 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_1_0.place(x=57, y=158)

btn_1_1 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_1_1.place(x=183, y=158)

btn_1_2 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_1_2.place(x=310, y=158)

# Btns linha 2
btn_2_0 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_2_0.place(x=57, y=287)

btn_2_1 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_2_1.place(x=183, y=287)

btn_2_2 = Button(frame_baixo, text="", width=3, font=("Ivy 45 bold"), overrelief=RIDGE, relief="flat", bg=fundo, fg=branco)
btn_2_2.place(x=310, y=287)


janela.mainloop()

# Vídeo usado como base: https://youtu.be/8qqeHip4NZQ?si=iTEzdmpLj4lpgPjn