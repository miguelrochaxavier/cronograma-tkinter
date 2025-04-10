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
        
        #Label com uma foto na parte superior do app em cima do título
        #
        #
        #

        #Label título parte superior do app
        self.resultado_label = CTkLabel(master=self, text="hábitos com tkinter", font=("Arial", 32, "bold"))
        self.resultado_label.place(relx=0.12, rely=0.19, anchor='center')
        
        #Label com uma foto na parte superior da frase motivacional do app 
        self.img = CTkImage(Image.open('icon-bar_frasemotivacional.png'), size=(20,20))
        self.label = CTkLabel(self, image=self.img, text="", bg_color='transparent')
        self.label.pack(pady=20)
        self.label.place(relx=0.046, rely=0.25, anchor='center')

        #Label frase motivacional na parte superior do app
        self.resultado_label = CTkLabel(master=self, text="A gratidão é uma grande aliada do sucesso!", font=("Arial", 16, "italic"), fg_color="#fff0b3")
        self.resultado_label.place(relx=0.14, rely=0.25, anchor='center')



if __name__ == "__main__":
    app = CronogramaFullScreen()
    app.mainloop() 