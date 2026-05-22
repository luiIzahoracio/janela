import tkinter as tk

app = tk.Tk()

app.title("minha janela simples")
app.geometry("400x300")


label = tk.Label(app, text="uma janela")
label.pack(pady=50)

app.mainloop()  