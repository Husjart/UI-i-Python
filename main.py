import tkinter as tk
from tkinter import messagebox
import subprocess

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()

def update_text(new_text):
    text_box.delete('1.0', tk.END)  # Slet alt indhold fra tekstboksen
    text_box.insert('1.0', new_text)  # Indsæt ny tekst

def run_powershell_script(script_path):
    # Kører PowerShell-scriptet i baggrunden
    subprocess.Popen(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path])

def tekst1():
    update_text('Dette script kopiere filer fra backup1\nog over til backup2')
    run_powershell_script(r"C:\Users\Morten M. Hansen\Desktop\test2.ps1")  # Ændr stien til dit PowerShell-script

def tekst2():
    update_text('Åbner CMD')
    run_powershell_script(r"C:\Users\Morten M. Hansen\Desktop\open cmd.ps1")  # Hvis du ønsker at køre script ved denne knap også

def tekst3():
    update_text('Generere en liste over alle filer i \nden angivne mappe og gemme denne \nliste i en tekstfil. ')
    run_powershell_script(r"C:\Users\Morten M. Hansen\Desktop\Ny mappe.ps1")  # Hvis du ønsker at køre script ved denne knap også

# Opret vinduet
root = tk.Tk()
root.geometry('500x500-5+40')
root.title("Simpelt Tkinter eksempel")

# Opret frame om knapperne
frame = tk.Frame(root, borderwidth=5, relief="ridge", width=100, height=300)

# Opret tekstbox i højre side
text_box = tk.Text(root, width=40, height=10)
text_box.grid(row=0, column=1, rowspan=1, padx=10, pady=5)

# Opret knapper
button = tk.Button(root, text="Klik på mig", command=on_button_click)
knap1 = tk.Button(root, text="Backup", command=tekst1)
knap2 = tk.Button(root, text="CMD", command=tekst2)
knap3 = tk.Button(root, text="Ny mappe", command=tekst3)
btn_close = tk.Button(root, text="Luk vinduet", command=close_window)

# Hvor skal knapperne være?
button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne
knap1.grid(row=1, column=0, padx=10, pady=5)
knap2.grid(row=2, column=0, padx=10, pady=5)
knap3.grid(row=3, column=0, padx=10, pady=5)
btn_close.grid(row=8, column=1, padx=10, pady=10)

frame.grid(column=0, row=0, columnspan=1, rowspan=4)

# Start Tkinter event loop
root.mainloop()
