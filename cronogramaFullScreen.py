from customtkinter import *
from PIL import Image

class CronogramaFullScreen(CTkToplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.geometry('1100x580')
        self.title('Cronograma FullScreen - v.0.01')
        self.stats_frame = CTkFrame(master=self, fg_color="transparent")
        self.stats_frame.pack(padx=(54, 0), pady=(18, 0), anchor="nw")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #Label com uma foto na parte superior do app em cima do título // 1920x191 - Banner
        self.img = CTkImage(Image.open('banner.png'), size=(2115,200)) #ValorUm = x; ValorDois = y;
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.45, rely=0.05, anchor='center')

        #Label título parte superior do app
        self.resultado_label = CTkLabel(master=self, text="hábitos com tkinter", font=("Arial", 32, "bold"))
        self.resultado_label.place(relx=0.12, rely=0.19, anchor='center')
        
        #Label com uma foto na parte superior da frase motivacional do app 
        self.img = CTkImage(Image.open('icon-bar_frasemotivacional.png'), size=(60,100))
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.046, rely=0.25, anchor='center')

        #Label frase motivacional na parte superior do app
        self.resultado_label = CTkLabel(master=self, text="A gratidão é uma grande aliada do sucesso!", font=("Arial", 16, "italic")) #, fg_color="#ffffb3"
        self.resultado_label.place(relx=0.14, rely=0.25, anchor='center')

        #Label com uma bar divisoria
        self.img = CTkImage(Image.open('icon-bar-maxsize.png'), size=(2115,21)) #ValorUm = x; ValorDois = y;
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.43, rely=0.35, anchor='center')

        #Label Three bars mais nome do mês abaixo da label bar divisoria
        self.img = CTkImage(Image.open('icon-threebar.png'), size=(40,70))
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.051, rely=0.40, anchor='center')

        #Label texto do mês
        self.resultado_label = CTkLabel(master=self, text="hábitos de ABRIL", font=("Arial", 28, "bold")) 
        self.resultado_label.place(relx=0.12, rely=0.4, anchor='center')
        
        #Label com títulos
        self.resultado_label = CTkLabel(master=self, text="Dias da semana", font=("Arial", 16))
        self.resultado_label.place(relx=0.07, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="💡Qualidade de Sono", font=("Arial", 16))
        self.resultado_label.place(relx=0.17, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="🔱Humor ...", font=("Arial", 16))
        self.resultado_label.place(relx=0.26, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅comer", font=("Arial", 16))
        self.resultado_label.place(relx=0.36, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅acordar cedo", font=("Arial", 16))
        self.resultado_label.place(relx=0.44, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅estudar escola", font=("Arial", 16))
        self.resultado_label.place(relx=0.52, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅estudar enem", font=("Arial", 16))
        self.resultado_label.place(relx=0.6, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="💧2L água", font=("Arial", 16))
        self.resultado_label.place(relx=0.68, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="#programar", font=("Arial", 16))
        self.resultado_label.place(relx=0.76, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅leitura", font=("Arial", 16))
        self.resultado_label.place(relx=0.84, rely=0.48, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="✅rezar e med...", font=("Arial", 16))
        self.resultado_label.place(relx=0.92, rely=0.48, anchor='center')

        #Label dias da semana
        self.resultado_label = CTkLabel(master=self, text="Domingo", font=("Arial", 16))
        self.resultado_label.place(relx=0.057, rely=0.52, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Segunda-feira", font=("Arial", 16))
        self.resultado_label.place(relx=0.063, rely=0.57, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Terça-feira", font=("Arial", 16))
        self.resultado_label.place(relx=0.058, rely=0.62, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Quarta-feira", font=("Arial", 16))
        self.resultado_label.place(relx=0.058, rely=0.67, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Quinta-feira", font=("Arial", 16))
        self.resultado_label.place(relx=0.058, rely=0.72, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Sexta-feira", font=("Arial", 16))
        self.resultado_label.place(relx=0.058, rely=0.77, anchor='center')
        self.resultado_label = CTkLabel(master=self, text="Sábado", font=("Arial", 16))
        self.resultado_label.place(relx=0.053, rely=0.82, anchor='center')

        #Label qualidade de sono
        self.btn = CTkComboBox(master=self, values=['', 'bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.52, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.57, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.62, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.67, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.72, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.77, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','bom', 'mediano', 'ruim', 'madruguei']) 
        self.btn.place(relx=0.166, rely=0.82, anchor='center')

        #Label humor
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.52, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.57, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.62, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.67, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.72, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.77, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
        self.btn.place(relx=0.273, rely=0.82, anchor='center')

        #Label comer ao acordar
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.421, rely=0.82, anchor='center')

        #Label acordar cedo
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.488, rely=0.82, anchor='center')

        #Label estudar escola
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.568, rely=0.82, anchor='center')

        #Label estudar enem
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.647, rely=0.82, anchor='center')

        #Label qtd L de água
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.52, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.57, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.62, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.67, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.72, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.77, anchor='center')
        self.btn = CTkComboBox(master=self, values=['','💧', '💧💧', '💧💧💧', '💧++'],fg_color='#66c2ff')
        self.btn.place(relx=0.69, rely=0.82, anchor='center')

        #Label programar
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.82, rely=0.82, anchor='center')

        #Label leitura
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.9, rely=0.82, anchor='center')

        #Label rezar e meditar
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.52, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.57, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.62, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.67, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.72, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.77, anchor='center')
        self.check = CTkCheckBox(master=self, text='', width=300)
        self.check.place(relx=0.966, rely=0.82, anchor='center')


        
if __name__ == "__main__":
    app = CronogramaFullScreen()
    app.mainloop() 