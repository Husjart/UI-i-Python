import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def tekst1():
    
    
def tekst2():
    
    
def tekst3():
    

def close_window():
    root.destroy()

# Opret vinduet
root = tk.Tk()
root.geometry('300x200-5+40')
root.title("Simpelt Tkinter eksempel")

# Opret en knap
button = tk.Button(root, text="Klik på mig", command=on_button_click)
knap1 = tk.Button(root, text="1", tekst1)
knap2 = tk.Button(root, text="2", tekst2)
knap3 = tk.Button(root, text="3", tekst3)
btn_close = tk.Button(root, text="Luk vindet", command=close_window)

# Hvor skal knappen være?
button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne
knap1.grid(row=1, column=0, padx=10, pady=5)
knap2.grid(row=2, column=0, padx=10, pady=5)
knap3.grid(row=3, column=0, padx=10, pady=5)
btn_close.grid(row=8, column=1, padx=10, pady=10)  

# Start Tkinter event loop
root.mainloop()




