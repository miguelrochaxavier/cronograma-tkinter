from customtkinter import *
from PIL import Image

class Cronograma(CTkToplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.geometry('500x800')
        self.resizable(0,0)
        self.title('Cronograma com Tkinter - v.0.01')
        self.stats_frame = CTkFrame(master=self, fg_color="transparent")
        self.stats_frame.pack(padx=(54, 0), pady=(18, 0), anchor="nw")

        self.img = CTkImage(Image.open('icon-rindoios.png'), size=(50,50))
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.15, rely=0.07, anchor='center')

        self.btn = CTkComboBox(master=self, values=['Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.25, rely=0.14, anchor='center')

        self.btn = CTkComboBox(master=self, values=['bom', 'mediano', 'ruim', 'madruguei'], fg_color="green") #fg_color="green muda o fundo
        self.btn.place(relx=0.25, rely=0.19, anchor='center')

        self.check = CTkCheckBox(master=self, text='✅comer', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.24, anchor='center')

        self.check = CTkCheckBox(master=self, text='✅acordar cedo', width=300)
        self.check.place(relx=0.41, rely=0.29, anchor='center')

        self.check = CTkCheckBox(master=self, text='❗estudar escola', width=300)
        self.check.place(relx=0.41, rely=0.34, anchor='center')

        self.check = CTkCheckBox(master=self, text='❗estudar enem', width=300)
        self.check.place(relx=0.41, rely=0.39, anchor='center')

        self.check = CTkCheckBox(master=self, text='💧2L água', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.44, anchor='center')

        self.check = CTkCheckBox(master=self, text='✅treino', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.49, anchor='center')

        self.check = CTkCheckBox(master=self, text='#programar', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.54, anchor='center')

        self.check = CTkCheckBox(master=self, text='✅leitura', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.59, anchor='center')

        self.check = CTkCheckBox(master=self, text='✅rezar e med...', width=300) #rely = 0.05 de distância entre um e outro.
        self.check.place(relx=0.41, rely=0.64, anchor='center')

    def on_closing(self):
        self.destroy() 

    def change_fg_color(self):
        self