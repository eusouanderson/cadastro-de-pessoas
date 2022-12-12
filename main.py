import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Cadastro de Nome e Email')
        self.geometry("300x300")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        global cont
        padding = {'padx': 5, 'pady': 5}

        # label
        ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)
        ttk.Label(self, text='Email:').grid(column=0, row=1, **padding)

        # Entry
        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry.focus()

        email_entry = ttk.Entry(self, textvariable=self.email_var)
        email_entry.grid(column=1, row=1, **padding)
        email_entry.focus()


        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=1, **padding)
        cont = 6
        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=cont, columnspan=5, **padding)


    def submit(self):
        global cont

        cont += 1
        while True:
            self.output_label.config(text=' Nome: ' + self.name_var.get() + ' Email: ' + self.email_var.get())
            self.output_label = ttk.Label(self)
            self.output_label.grid(column=0, row=cont, columnspan=5)
            self.name_var.set('')
            self.email_var.set('')
            break

if __name__ == "__main__":
    app = App()
    app.mainloop()