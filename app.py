# pip install customtkinter no powershell
from customtkinter import *

app = CTk()
app.geometry('500x800')
app.resizable(0,0)
app.title('Cronograma com Tkinter')

CTkLabel(master=app, text="Cronograma com Tkinter", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))
stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

btn = CTkComboBox(master=app, values=['Feliz', 'Normal', 'Bravo', 'Triste'])
btn.place(relx=0.25, rely=0.14, anchor='center')

check = CTkCheckBox(master=app, text='✅estudar', width=300)
check.place(relx=0.41, rely=0.19, anchor='center')

check = CTkCheckBox(master=app, text='✅comer', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.41, rely=0.24, anchor='center')

app.mainloop()