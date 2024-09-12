import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()
    
# Opret vinduet
root = tk.Tk()
root.geometry('500x500-5+40')
root.title("Simpelt Tkinter eksempel")

# Opret frame om knapperne
frame = tk.Frame(root, borderwidth=5, relief="ridge", width=100, height=300)

# Opret tekstbox i højre side
text_box = tk.Text(root, width=40, height=10)
text_box.grid(row=0, column=1, rowspan=1, padx=10, pady=5)
# Opret en knap
button = tk.Button(root, text="Klik på mig", command=on_button_click)
knap1 = tk.Button(root, text="1", command=on_button_click)
knap2 = tk.Button(root, text="2", command=on_button_click)
knap3 = tk.Button(root, text="3", command=on_button_click)
btn_close = tk.Button(root, text="Luk vinduet", command=close_window)

# Hvor skal knappen være?
button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne
knap1.grid(row=1, column=0, padx=10, pady=5)
knap2.grid(row=2, column=0, padx=10, pady=5)
knap3.grid(row=3, column=0, padx=10, pady=5)
btn_close.grid(row=8, column=1, padx=10, pady=10)  

frame.grid(column=0, row=0, columnspan=1, rowspan=4)


# Start Tkinter event loop
root.mainloop()




