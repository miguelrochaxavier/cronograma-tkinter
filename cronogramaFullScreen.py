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
        
        self.resultado_label = CTkLabel(master=self, text="hábitos com tkinter", font=("Arial", 32, "bold"))
        self.resultado_label.place(relx=0.12, rely=0.19, anchor='center')

if __name__ == "__main__":
    app = CronogramaFullScreen()
    app.mainloop() 