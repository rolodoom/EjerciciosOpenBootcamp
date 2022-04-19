#  _______   _______
# |  _____| |  ___  |
# | |       | |   | |    Rolando Ramos Torres (@rolodoom)
# | |       | |___| |    https://github.com/rolodoom
# |_|       |_______|
#  _         _______
# | |       |  ___  |
# | |       | |   | |    Sesion 10 - GUI
# | |_____  | |___| |    Ejercicio 1
# |_______| |_______|
#
#

# En este ejercicio tenéis que crear una lista de RadioButton
# que muestre la opción que se ha seleccionado y que contenga
# un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.


# Importar Módulos
import tkinter as tk
from tkinter import ttk


def main():
    # Funciones auxiliares
    def seleccionar():
        display.config(text=f"{seleccion.get()}")

    def limpiar():
        seleccion.set(None)
        display.config(text="Escoge tu equipo favorito!")

    # Se crea la instancia de la clase Tk
    window = tk.Tk()
    window.title("S10 - E01")
    window.geometry("300x180")
    window.resizable(0, 0)

    # Configurar el grid
    window.columnconfigure(0, weight=1)

    # Display
    display = tk.Label(
        window,
        text="Escoge tu equipo favorito!",
        bg="#999",
        fg="#333",
        width=300,
        height=3,
    )
    display.grid(column=0, row=0, pady=(0, 10), sticky=tk.W)

    # Seleccion

    seleccion = tk.StringVar()
    seleccion.set(None)
    sel1 = tk.Radiobutton(
        window,
        text="FC Barcelona",
        value="FC Barcelona",
        variable=seleccion,
        command=seleccionar,
    )
    sel2 = tk.Radiobutton(
        window,
        text="Real Madrid C.F.",
        value="Real Madrid C.F.",
        variable=seleccion,
        command=seleccionar,
    )
    sel3 = tk.Radiobutton(
        window,
        text="Valencia CF",
        value="Valencia CF",
        variable=seleccion,
        command=seleccionar,
    )

    sel1.grid(column=0, row=1, sticky=tk.W)
    sel2.grid(column=0, row=2, sticky=tk.W)
    sel3.grid(column=0, row=3, sticky=tk.W)

    # Boton Limpiar
    limpiar_button = tk.Button(window, text="Limpiar", command=limpiar)
    limpiar_button.grid(column=0, row=4, pady=5)

    # Mostrar la ventana
    window.mainloop()


if __name__ == "__main__":
    main()
