from customtkinter import *
from PIL import Image
from tkcalendar import Calendar
from datetime import date

class Cronograma(CTkToplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.geometry('500x800')
        self.resizable(0,0)
        self.title('Cronograma com Tkinter')

        self.stats_frame = CTkFrame(master=self, fg_color="transparent")
        self.stats_frame.pack(padx=(54, 0), pady=(18, 0), anchor="nw")

        # enfiar o text='' vazio em algum lugar da label para tirar o CtkImage da frente do icone
        self.img = CTkImage(Image.open('icon-booksios.png'), size=(50,50))
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.15, rely=0.07, anchor='center')

        self.cal = Calendar(self, selectmode='day', year=2025, month=3, day=19) #Fazer um código que indetifica automaticamente que dia e mês atual
        self.cal.pack(pady=20) #Fazer o mesmo para horário
        self.cal.place(relx=0.35, rely=0.7, anchor='center')

        self.btn = CTkComboBox(master=self, values=['Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.25, rely=0.14, anchor='center')

        self.btn = CTkComboBox(master=self, values=['bom', 'mediano', 'ruim', 'madruguei'])
        self.btn.place(relx=0.25, rely=0.19, anchor='center')

        self.resultado_label = CTkLabel(master=self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.6, anchor='center')

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

        self.entry = CTkEntry(master=self, placeholder_text='Escreva aqui...', width=300,)
        self.entry.place(relx=0.39, rely=0.85, anchor='center')

        self.btn = CTkButton(master=self, text='Adicionar Tarefa', width=30, command=self.resposta_adicionar)
        self.btn.place(relx=0.81, rely=0.85, anchor='center')

        self.resultado_label = CTkLabel(master=self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.42, rely=0.92, anchor='center')

    def resposta_adicionar(self):
        resposta = str(self.entry.get())
        self.resultado_label.configure(text=f'• {resposta}')

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = Cronograma()
    app.mainloop() 