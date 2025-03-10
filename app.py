# pip install customtkinter no powershell
from customtkinter import *

app = CTk()
app.geometry('500x800')
app.resizable(0,0)
app.title('Cronograma')

CTkLabel(master=app, text="Cronograma com Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

btn = CTkComboBox(master=app, values=['Feliz', 'Normal', 'Bravo', 'Triste'])
btn.place(relx=0.23, rely=0.14, anchor='center')

check = CTkCheckBox(master=app, text='Teste 01', width=300)
check.place(relx=0.4, rely=0.2, anchor='center')

check = CTkCheckBox(master=app, text='Teste 02', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.4, rely=0.25, anchor='center')

app.mainloop()