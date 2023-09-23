import tkinter as tk
# 1 - Criando janela
window = tk.Tk()
window.geometry("300x150")
window.title('Frases')

# 2 - adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - adicionando o label
label = tk.Label(frame, text='tomeeee')
label.pack(fill='x', expand=True)

# 4 - adicionando o input text
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())


# 6 - adicionando botão
button = tk.Button(frame, text='Enviar', command=click)
button.pack()

window.mainloop() 