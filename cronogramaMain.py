import customtkinter as ctk
from cronogramaPage import Cronograma
from cronogramaFullScreen import CronogramaFullScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        self.title("Home - Cronograma com Tkinter")
        
        # Botão para abrir o Cronograma
        self.btn = ctk.CTkButton(self, text="Abrir Cronograma Windowed - v.0.01", command=self.open_cronograma)
        self.btn.pack(pady=20)
        self.btn.place(relx=0.51, rely=0.3, anchor='center')

        self.btn = ctk.CTkButton(self, text="Abrir Cronograma FullScreen - v.0.01", command=self.open_cronograma_fullscreen)
        self.btn.pack(pady=20)
        self.btn.place(relx=0.51, rely=0.5, anchor='center')
        
    def open_cronograma(self):
        # Cria uma nova instância do Cronograma passando self como parent
        cronograma = Cronograma(self)
        cronograma.wait_window()  # Espera a janela do Cronograma fechar

    def open_cronograma_fullscreen(self):
        cronograma = CronogramaFullScreen(self)
        cronograma.wait_window()

if __name__ == "__main__":
    app = App()
    app.mainloop() 