import tkinter as tk



window = tk.Tk()
window.title("Confirmar usuario")
window.geometry("100x100")
title = tk.Label(text ="Ingrese su contraseña")
title.grid(column = 2, row = 5)

b1 = tk.Button(text = "Aceptar")
b1.grid(column = 0, row = 2)

b2 = tk.Button(text = "Cancelar")
b2.grid(column = 1, row = 2)

input1 = tk.Entry()
input1.grid(column = 0, row = 1)

window.mainloop()
