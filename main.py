import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100  # Converter de cm para metros
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"

        resultado_texto = f"IMC: {imc:.2f}\nCategoria: {categoria}"
        label_resultado.config(text=resultado_texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")


def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="Resultado")


def sair():
    root.destroy()


# Criação da janela principal
root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")

# Widgets
tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_endereco = tk.Entry(root, width=40)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Altura (cm):").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
entry_altura = tk.Entry(root, width=20)
entry_altura.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

tk.Label(root, text="Peso (Kg):").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
entry_peso = tk.Entry(root, width=20)
entry_peso.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)

label_resultado = tk.Label(root, text="Resultado", width=40, height=5, relief="sunken", anchor="w")
label_resultado.grid(row=2, column=2, rowspan=2, padx=10, pady=5)

# Botões
tk.Button(root, text="Calcular", command=calcular_imc).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Reiniciar", command=reiniciar).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Sair", command=sair).grid(row=4, column=2, padx=10, pady=10)

# Execução da janela
root.mainloop()
