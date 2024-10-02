import serial
import tkinter as tk
from tkinter import messagebox

# Configurar el puerto serie
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)  # Asegúrate de que 'COM8' es el puerto correcto
except:
    messagebox.showerror("Error", "No se pudo conectar al puerto COM8")

# Función para encender el LED
def turn_on_led():
    if arduino.isOpen():
        arduino.write(b'1')  # Enviar '1' para encender el LED

# Función para apagar el LED
def turn_off_led():
    if arduino.isOpen():
        arduino.write(b'0')  # Enviar '0' para apagar el LED

# Función para cerrar el programa y el puerto serial
def on_closing():
    if arduino.isOpen():
        arduino.close()  # Cerrar el puerto serial al salir
    root.destroy()  # Cerrar la ventana de Tkinter

# Crear la ventana principal con Tkinter
root = tk.Tk()
root.title("Control de LED con Arduino")

# Botón para encender el LED
btn_on = tk.Button(root, text="Encender LED", command=turn_on_led, bg="green", fg="white", font=("Helvetica", 12))
btn_on.pack(pady=10)

# Botón para apagar el LED
btn_off = tk.Button(root, text="Apagar LED", command=turn_off_led, bg="red", fg="white", font=("Helvetica", 12))
btn_off.pack(pady=10)

# Manejar el cierre de la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Ejecutar el loop principal de la ventana
root.mainloop()
