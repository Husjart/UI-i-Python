import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()

# Opret vinduet
root = tk.Tk()
root.geometry('300x200-5+40')
root.title("Simpelt Tkinter eksempel")

# Opret en knap
button = tk.Button(root, text="Klik på mig", command=on_button_click)
btn_close = tk.Button(root, text="Luk vindet", command=close_window)


button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne
btn_close.grid(row=0, column=1, padx=10, pady=10)  




# Start Tkinter event loop
root.mainloop()



# button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne


