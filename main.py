import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.pessoa = []
        self.email = []
        self.grupo = dict()
        self.title('Cadastro de Nome e Email')
        self.geometry("400x400")
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.contatc_var = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):

        self.padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Name:').grid(column=0, row=0, **self.padding)
        ttk.Label(self, text='Email:').grid(column=0, row=1, **self.padding)
        # Entry
        self.name_entry = ttk.Entry(self, textvariable=self.name_var)
        self.name_entry.grid(column=1, row=0, **self.padding)
        self.name_entry.focus()
        email_entry = ttk.Entry(self, textvariable=self.email_var)
        email_entry.grid(column=1, row=1, **self.padding)

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=1, **self.padding)

        search_button = ttk.Button(self, text='Search', command=self.search)
        search_button.grid(column=2, **self.padding)


        self.cont = 6
        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=self.cont, columnspan=5, **self.padding)

    def submit(self):

        self.cont += 1
        while True:
            self.output_label.config(text=' Nome: ' + self.name_var.get().upper() + ' Email: ' + self.email_var.get().upper())
            self.output_label = ttk.Label(self)
            self.output_label.grid(column=0, row=self.cont, columnspan=5)
            self.pessoa.append(self.name_var.get())
            self.email.append(self.email_var.get())
            self.grupo['Nomes'] = self.pessoa[:]
            self.grupo['Emails'] = self.email[:]
            self.name_var.set('')
            self.email_var.set('')
            tk.messagebox.showinfo('Cadastro', 'Cadastrado com sucesso!')
            break

    def search(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        root.title('Search')
        root.geometry("250x50")
        self.search_var = StringVar()

        #Entry
        self.search = ttk.Entry(root, textvariable=self.search_var)
        self.search.grid(column=1, row=0, **self.padding)

        #Output
        self.output_label.config(text=self.pessoa)
        self.output_label.grid(column=0, row=self.cont, columnspan=5)
        ...
if __name__ == "__main__":
    app = App()
    app.mainloop()