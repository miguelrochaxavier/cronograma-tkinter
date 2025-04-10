#      self.entry = CTkEntry(master=self, placeholder_text='Escreva aqui...', width=300,)
#        self.entry.place(relx=0.39, rely=0.85, anchor='center')
#
#        self.btn = CTkButton(master=self, text='Adicionar Tarefa', width=30, command=self.resposta_adicionar)
#        self.btn.place(relx=0.81, rely=0.85, anchor='center')
#
#        self.resultado_label = CTkLabel(master=self, text="", font=("Arial", 14))
#        self.resultado_label.place(relx=0.42, rely=0.92, anchor='center')
#
#    def resposta_adicionar(self):
#        resposta = str(self.entry.get())
#        self.resultado_label.configure(text=f'• {resposta}')
