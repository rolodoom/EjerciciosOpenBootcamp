#  _______   _______
# |  _____| |  ___  |
# | |       | |   | |    Rolando Ramos Torres (@rolodoom)
# | |       | |___| |    https://github.com/rolodoom
# |_|       |_______|
#  _         _______
# | |       |  ___  |
# | |       | |   | |    Sesion 10 - GUI
# | |_____  | |___| |    Ejercicio 2
# |_______| |_______|
#
#

# En este segundo ejercicio, tendréis que crear una interfaz sencilla
# la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.


# Importar Módulos
import tkinter as tk


def main():

    # Se crea la instancia de la clase Tk
    window = tk.Tk()
    window.title("S10 - E02")
    window.resizable(0, 0)

    # Display
    items = [
        "Debian",
        "Fedora",
        "ArchLinux",
        "OpenSUSE",
        "Ubuntu",
        "Elementary OS",
        "Linux Mint",
        "Manjaro",
    ]
    list_items = tk.StringVar(value=items)
    listbox = tk.Listbox(
        window,
        height=len(items),
        listvariable=list_items,
    )
    listbox.grid(
        column=0,
        row=0,
        sticky=tk.W,
        padx=10,
        pady=(15, 5),
    )

    # Label
    label = tk.Label(text="Linux Distros")
    label.grid(column=0, row=1, pady=(5, 15))

    # Mostrar la ventana
    window.mainloop()


if __name__ == "__main__":
    main()
