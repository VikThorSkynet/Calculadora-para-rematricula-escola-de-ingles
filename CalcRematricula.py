import tkinter as tk
from tkinter import ttk
import locale

# Configurar localização para formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def validar_numero(entrada):
    if entrada == "": return True
    try:
        # Permite vírgulas e pontos
        entrada = entrada.replace(',', '.')
        float(entrada)
        return True
    except ValueError:
        return False

def converter_para_float(texto):
    return float(texto.replace(',', '.'))

def formatar_moeda(valor):
    return locale.currency(valor, grouping=True, symbol=True)

def calcular():
    try:
        # Obtém os valores dos campos e converte
        primeiro_semestre = converter_para_float(entrada_primeiro.get())
        segundo_semestre = converter_para_float(entrada_segundo.get())
        # Se o campo de desconto estiver vazio, usa 0
        desconto_texto = entrada_desconto.get()
        desconto = converter_para_float(desconto_texto) if desconto_texto.strip() else 0

        # Calcula os valores
        valor_total = primeiro_semestre + segundo_semestre
        valor_com_desconto = valor_total - (valor_total * (desconto/100))

        # Limpa a área de resultado
        resultado_text.delete(1.0, tk.END)

        # Mostra os resultados
        resultado_text.insert(tk.END, f"Valor total: {formatar_moeda(valor_total)}\n")
        resultado_text.insert(tk.END, f"Valor com desconto: {formatar_moeda(valor_com_desconto)}\n\n")
        resultado_text.insert(tk.END, "Valores das parcelas:\n")

        # Calcula e mostra as parcelas
        for parcela in range(1, 14):
            valor_parcela = valor_com_desconto / parcela
            resultado_text.insert(tk.END, f"{parcela}x de {formatar_moeda(valor_parcela)}\n")

    except ValueError:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Por favor, insira valores numéricos válidos!")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora de Rematrícula by Vitão")
janela.geometry("600x700")

# Configurar estilo
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Criar e posicionar os elementos
frame = ttk.Frame(janela, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Validação para entrada de números
validacao = janela.register(validar_numero)

# Labels e campos de entrada
ttk.Label(frame, text="Primeiro Semestre (R$):", font=("Arial", 12, "bold")).grid(column=0, row=0, sticky=tk.W)
entrada_primeiro = ttk.Entry(frame, font=("Arial", 12), validate="key", validatecommand=(validacao, '%P'))
entrada_primeiro.grid(column=1, row=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Segundo Semestre (R$):", font=("Arial", 12, "bold")).grid(column=0, row=1, sticky=tk.W)
entrada_segundo = ttk.Entry(frame, font=("Arial", 12), validate="key", validatecommand=(validacao, '%P'))
entrada_segundo.grid(column=1, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Desconto (%):", font=("Arial", 12, "bold")).grid(column=0, row=2, sticky=tk.W)
entrada_desconto = ttk.Entry(frame, font=("Arial", 12), validate="key", validatecommand=(validacao, '%P'))
entrada_desconto.grid(column=1, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

# Botão de calcular
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular, style="TButton")
btn_calcular.grid(column=0, row=3, columnspan=2, pady=20)

# Área de resultado
resultado_text = tk.Text(frame, height=20, width=50, font=("Arial", 12))
resultado_text.grid(column=0, row=4, columnspan=2, pady=10)

# Scrollbar para a área de resultado
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=resultado_text.yview)
scrollbar.grid(column=2, row=4, sticky=(tk.N, tk.S))
resultado_text.configure(yscrollcommand=scrollbar.set)

# Configurar redimensionamento
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Iniciar o loop da interface
janela.mainloop()
