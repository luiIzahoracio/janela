import tkinter as tk

def mostrar_texto():
    texto_digitado = entrada.get()
    rotulo.config(text=f"Você digitou: {texto_digitado}")


app = tk.Tk()
app.title("Janela com entrada e botão")
app.geometry("400x250")


entrada = tk.Entry(app, font=("Arial", 12), width=25)
entrada.pack(pady=15)

botao = tk.Button(
    app, text="Enviar", font=("Arial", 10), command = mostrar_texto
)
botao.pack(pady=10)

rotulo = tk.Label(app, text="", font=("Arial", 12, "bold"))
rotulo.pack(pady=15)

app.mainloop()