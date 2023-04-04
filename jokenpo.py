import customtkinter as ctk
from PIL import Image
import os
import random
from tkinter import messagebox
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")

img_pedra = ctk.CTkImage(
    Image.open(os.path.join(image_path,
                            "Images/pedra.jpeg")),
    size=(90, 90)
)

img_papel = ctk.CTkImage(
    Image.open(os.path.join(image_path,
                            "Images/papel.jpeg")),
    size=(90, 90)
)

img_tesoura = ctk.CTkImage(
    Image.open(os.path.join(image_path,
                            "Images/tesoura.jpg")),
    size=(90, 90)
)

class JokenpoTela(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('jokenpo')
        self.frame_jogo = ctk.CTkFrame(self,width=500,height=500)
        self.frame_jogo.pack()
        self.lbl_nomejogo = ctk.CTkLabel(self.frame_jogo, text='JOKENPO',font=('Roboto',22))
        self.lbl_nomejogo.place(rely=0.1,relx=0.4)

        self.combox_opcoes = ctk.CTkComboBox(self.frame_jogo, values=('Tesoura','Pedra','Papel'))
        self.combox_opcoes.place(relx=0.35,rely=0.4)
        self.lbl_jogador = ctk.CTkLabel(self.frame_jogo, text='Jogador', font=('Roboto',19))
        self.lbl_jogador.place(relx=0.15,rely=0.83)
        self.lbl_maquina = ctk.CTkLabel(self.frame_jogo, text='Maquina', font=('Roboto',19))
        self.lbl_maquina.place(relx=0.68,rely=0.83)
        self.lbl_versus = ctk.CTkLabel(self.frame_jogo, text='VS', font=('Roboto', 19))
        self.lbl_versus.place(rely=0.83,relx=0.45)
        self.btn_jogar = ctk.CTkButton(
            self.frame_jogo,
            text='play',
            font=('Roboto', 19),
            command=lambda: self.jogar(self.combox_opcoes.get())
        )
        self.btn_jogar.place(relx=0.35, rely=0.5)

        self.mainloop()



    def jogar(self,opc_usuario):

        if opc_usuario == 'Pedra':
            self.lbl_escolhajogador = ctk.CTkLabel(self.frame_jogo, text='', image=img_pedra)
            self.lbl_escolhajogador.place(relx=0.15, rely=0.63)
        elif opc_usuario == 'Papel':
            self.lbl_escolhajogador = ctk.CTkLabel(self.frame_jogo, text='', image=img_papel)
            self.lbl_escolhajogador.place(relx=0.15, rely=0.63)
        else:
            self.lbl_escolhajogador = ctk.CTkLabel(self.frame_jogo, text='', image=img_tesoura)
            self.lbl_escolhajogador.place(relx=0.15, rely=0.63)

        jokenpo = ['Pedra', 'Papel', 'Tesoura']
        opcao_maq = random.choice(jokenpo)

        if opcao_maq == 'Pedra':
            self.lbl_maquinarandom = ctk.CTkLabel(self.frame_jogo,text='', image=img_pedra)
            self.lbl_maquinarandom.place(relx=0.68, rely=0.63)
        elif opcao_maq == 'Papel':
            self.lbl_maquinarandom = ctk.CTkLabel(self.frame_jogo,text='', image=img_papel)
            self.lbl_maquinarandom.place(relx=0.68, rely=0.63)
        else:
            self.lbl_maquinarandom = ctk.CTkLabel(self.frame_jogo, text='', image=img_tesoura)
            self.lbl_maquinarandom.place(relx=0.68, rely=0.63)

        self.comparar_result(opc_usuario,opcao_maq)
        self.lbl_escolhajogador.place_forget()
        self.lbl_maquinarandom.place_forget()
    def comparar_result(self, jogador, maquina):
        print(jogador,maquina)
        if jogador == maquina:
            resultado ="empate!"
        elif (jogador == "Pedra" and maquina == "Tesoura") or (jogador == "Papel" and maquina == "Pedra") or (jogador == "Tesoura" and maquina == "Papel"):
             resultado ="voce venceu!"
        else:
            resultado = "voce perdeu!"


        messagebox.showinfo("resultado", resultado)








