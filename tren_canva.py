from tkinter import *

#-------------------
# Variables globales
#-------------------
BASE = 460
ALTURA = 220

#-------------------
# ventana principal
#-------------------

ventana_principal = Tk()
ventana_principal.title("Tren")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")
 
#---------------------
# frame de graficacion
#---------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="red", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas
c = Canvas(frame_graficacion,width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="blue", width=480, height=230)
frame_controles.place(x=10,y=260)

# creacion tren
rect_1 = c.create_rectangle(BASE/1.3,ALTURA/3,BASE/2.3,ALTURA/4, fill="gray67")
rect_3 = c.create_rectangle(BASE/1.2,ALTURA/1.4,BASE/4,ALTURA/2, fill="gray67")
circ_1 = c.create_oval(BASE/2-20,ALTURA/1.5,BASE/4,ALTURA, fill="saddle brown")
circ_2 = c.create_oval(BASE/1.7,ALTURA/1.5,BASE/1.3,ALTURA, fill="saddle brown")
rect_2 = c.create_rectangle(BASE/1.4-20,ALTURA/1.2+15,BASE/2-30,ALTURA/2+60, fill="bisque2")
rect_4 = c.create_rectangle(BASE/1.5,ALTURA/3,BASE/1.7-20,ALTURA/1.7-20, fill="gray92")
rect_5 = c.create_rectangle(BASE/4,ALTURA/5,BASE/3,ALTURA/2, fill="gray67")
rect_6 = c.create_rectangle(BASE/1.4,ALTURA/3,BASE/1.5,ALTURA/2, fill="gray67")
rect_7 = c.create_rectangle(BASE/1.8,ALTURA/3,BASE/2,ALTURA/2, fill="gray67")



#crear nombre
texto_1 = c.create_text(BASE/2, ALTURA/1.5, anchor="center", tex="German", font=("Arial", 20, "bold"), fill="cyan4", activefill="green yellow")
# CREAR VENTANA
ventana_principal.mainloop()