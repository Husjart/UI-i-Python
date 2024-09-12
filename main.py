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
root.geometry('500x500')
root.title("Simpelt Tkinter eksempel")

# Opret tekstbox i højre side
text_box = tk.Text(root, width=40, height=10)
text_box.grid(row=0, column=1, rowspan=4, padx=10, pady=5)

# Opret frame om knapperne
frame = tk.Frame(root, borderwidth=5, relief="ridge", width=100, height=300)

# Opret knapper
button = tk.Button(root, text="Klik på mig", command=on_button_click)
knap1 = tk.Button(root, text="Backup", command=tekst1)
knap2 = tk.Button(root, text="CMD", command=tekst2)
knap3 = tk.Button(root, text="Ny mappe", command=tekst3)
knap4 = tk.Button(root, text="?", command=on_button_click)
knap5 = tk.Button(root, text="?", command=on_button_click)
btn_close = tk.Button(root, text="Luk vinduet", command=close_window)

# Hvor skal knapperne være?
button.grid(row=0, column=0, padx=2, pady=0)  # Mindre afstand
knap1.grid(row=1, column=0, padx=2, pady=0)
knap2.grid(row=2, column=0, padx=5, pady=5)
knap3.grid(row=3, column=0, padx=5, pady=5)
knap4.grid(row=4, column=0, padx=5, pady=5)
knap5.grid(row=5, column=0, padx=5, pady=5)
btn_close.grid(row=6, column=0, padx=5, pady=5)  # Sørg for at den er i samme kolonne som de andre knapper

# Hvis du bruger en frame, kan du placere den efter knapperne
frame.grid(row=0, column=0, rowspan=6, padx=5, pady=5, sticky="ns")  # Eksempelvis
frame.grid_propagate(False)  # Gør frame størrelse statisk, så knapperne ikke påvirkes

# Start Tkinter event loop
root.mainloop()



"""DUPES
button = tk.Button(root, text="Klik på mig", command=on_button_click)

button.grid(row=0, column=0, padx=2, pady=0)

def tekst1():
    update_text('tilføj tekst')
    run_powershell_script(r"indsæt sti")
"""