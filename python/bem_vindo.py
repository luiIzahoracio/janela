import tkinter as tk

def mostrar_texto():
    texto_digitado = entrada.get()
    rotulo.config(text=f"entrouu")


app = tk.Tk()
app.title("Janela com entrada e botão")
app.geometry("500x300")
app.configure(bg="#FFE4E1")

label = tk.Label(app, text="vindo bem aqui")
label.pack(pady=5)


label = tk.Label(app, text="loga aqui")
label.pack(pady=5)
entrada = tk.Entry(app, font=("Arial", 12), width=25)
entrada.pack(pady=5)


rotulo = tk.Label(app, text="", font=("Arial", 12, "bold"))
rotulo.pack(pady=5)


label = tk.Label(app, text="bota a senha")
label.pack(pady=5)

entrada = tk.Entry(app, font=("Arial", 12), width=25)
entrada.pack(pady=5)

botao = tk.Button(
    app, text="Aperta", font=("Arial", 10), command = mostrar_texto
)
botao.pack(pady=5)

rotulo = tk.Label(app, text="", font=("Arial", 12, "bold"))
rotulo.pack(pady=5)

app.mainloop()