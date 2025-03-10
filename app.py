# pip install customtkinter no powershell
from customtkinter import *

app = CTk()
app.geometry('500x800')
app.resizable(0,0)
app.title('Cronograma')

CTkLabel(master=app, text="Cronograma com Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

app.mainloop()