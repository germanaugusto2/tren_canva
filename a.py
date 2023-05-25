import tkinter as tk

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dibujo de tren")
canvas = tk.Canvas(ventana, width=600, height=400)
canvas.pack()

# Dibujo del tren
canvas.create_rectangle(50, 250, 550, 350, fill="gray")  # Cuerpo del tren
canvas.create_rectangle(75, 200, 225, 250, fill="gray")  # Locomotora
canvas.create_oval(75, 275, 125, 325, fill="black")  # Rueda izquierda de la locomotora
canvas.create_oval(175, 275, 225, 325, fill="black")  # Rueda derecha de la locomotora

# Vagones
canvas.create_rectangle(275, 200, 425, 250, fill="gray")  # Vagón 1
canvas.create_oval(275, 275, 325, 325, fill="black")  # Rueda izquierda del vagón 1
canvas.create_oval(375, 275, 425, 325, fill="black")  # Rueda derecha del vagón 1

canvas.create_rectangle(475, 200, 625, 250, fill="gray")  # Vagón 2
canvas.create_oval(475, 275, 525, 325, fill="black")  # Rueda izquierda del vagón 2
canvas.create_oval(575, 275, 625, 325, fill="black")  # Rueda derecha del vagón 2

# Nombre en el centro del tren
nombre = "Su Nombre"
canvas.create_text(300, 275, text=nombre, font=("Arial", 14), fill="white")

ventana.mainloop()