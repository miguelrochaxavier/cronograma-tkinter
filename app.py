from customtkinter import *
from PIL import Image
from tkcalendar import Calendar

def resposta_adicionar() :
    resposta = str(entry.get())
    resultado_label.configure(text=f'• {resposta}')

app = CTk()
app.geometry('500x800')
app.resizable(0,0)
app.title('Cronograma com Tkinter')

stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

img = CTkImage(Image.open('icon-booksios.png'), size=(50,50))
label = CTkLabel(app, image=img, bg_color='transparent')
label.pack(pady=20)
label.place(relx=0.15, rely=0.07, anchor='center')

cal = Calendar(app, selectmode='day', year=2025, month=3, day=10) #Fazer um código que indetifica automaticamente que dia e mês atual
cal.pack(pady=20) #Fazer o mesmo para horário
cal.place(relx=0.35, rely=0.7, anchor='center')


btn = CTkComboBox(master=app, values=['Feliz😁', 'Normal😒', 'Bravo😡', 'Triste😭'])
btn.place(relx=0.25, rely=0.14, anchor='center')

btn = CTkComboBox(master=app, values=['bom', 'mediano', 'ruim', 'madruguei'])
btn.place(relx=0.25, rely=0.19, anchor='center')

resultado_label = CTkLabel(master=app, text="", font=("Arial", 14))
resultado_label.place(relx=0.5, rely=0.6, anchor='center')

check = CTkCheckBox(master=app, text='✅comer', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.41, rely=0.24, anchor='center')

check = CTkCheckBox(master=app, text='✅acordar cedo', width=300)
check.place(relx=0.41, rely=0.29, anchor='center')

check = CTkCheckBox(master=app, text='❗estudar escola', width=300)
check.place(relx=0.41, rely=0.34, anchor='center')

check = CTkCheckBox(master=app, text='❗estudar enem', width=300)
check.place(relx=0.41, rely=0.39, anchor='center')

check = CTkCheckBox(master=app, text='💧2L água', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.41, rely=0.44, anchor='center')

check = CTkCheckBox(master=app, text='✅treino', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.41, rely=0.49, anchor='center')

check = CTkCheckBox(master=app, text='#programar', width=300) #rely = 0.05 de distância entre um e outro.
check.place(relx=0.41, rely=0.54, anchor='center')

entry = CTkEntry(master=app, placeholder_text='Escreva aqui...', width=300,)
entry.place(relx=0.39, rely=0.85, anchor='center')

btn = CTkButton(master=app, text='Adicionar Tarefa', width=30, command=resposta_adicionar)
btn.place(relx=0.81, rely=0.85, anchor='center')

resultado_label = CTkLabel(master=app, text="", font=("Arial", 14))
resultado_label.place(relx=0.42, rely=0.92, anchor='center')

app.mainloop()