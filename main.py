import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()

def tekst1():
    text_box.delete('1.0', tk.END)
    text_box.insert('1.0', 'here is my\ntext to insert')
    
def tekst2():
    text_box.delete('1.0', tk.END)
    text_box.insert('1.0', 'mere lort')

def tekst3():
    text_box.delete('1.0', tk.END)
    text_box.insert('1.0', 'lort')

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
knap1 = tk.Button(root, text="Indsæt tekst", command=tekst1)
knap2 = tk.Button(root, text="2", command=tekst2)
knap3 = tk.Button(root, text="3", command=tekst3)
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




