import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set('Hello World')

        ttk.Label(self, text='Name:').grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.name).grid(row=0, column=1, sticky=(tk.W+tk.E))
        ttk.Button(self, text='Change', command=self.on_change).grid(row=0, column=2, sticky=tk.E)
        ttk.Label(self, textvariable=self.hello_string, font=('TkDefaultFont', 64), wraplength=600).grid(row=1, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set('Hello ' + self.name.get())
        else:
            self.hello_string.set('Hello World')

class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Hello Tkinter')
        self.geometry('800x600')
        self.resizable(width=False, height=False)

        HelloView(self).grid(sticky=(tk.E+tk.W+tk.N+tk.S))
        self.columnconfigure(0, weight=1)

if __name__ == '__main__':
    MyApplication().mainloop()