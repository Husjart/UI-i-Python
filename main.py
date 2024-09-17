import tkinter as tk
from tkinter import messagebox
import subprocess

# Global variabel til at gemme scriptstien
current_script_path = None

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()

def update_text(new_text):
    text_box.delete('1.0', tk.END)  # Slet alt indhold fra tekstboksen
    text_box.insert('1.0', new_text)  # Indsæt ny tekst

def run_powershell_script(script_path):
    if script_path:
        try:
            result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], capture_output=True, text=True)
            if result.returncode != 0:
                messagebox.showerror("Fejl", f"Fejl ved kørsel af script: {result.stderr}")
        except Exception as e:
            messagebox.showerror("Fejl", f"En fejl opstod: {str(e)}")
    else:
        messagebox.showerror("Fejl", "Intet script valgt")
        
def tekst1():
    global current_script_path
    update_text('Dette script kopierer filer fra backup1\nog over til backup2')
    current_script_path = r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Backup script.ps1"

def tekst2():
    global current_script_path
    update_text('Åbner CMD')
    current_script_path = r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\open cmd.ps1"

def tekst3():
    global current_script_path
    update_text('Genererer en ny mappe på C:\\.')
    current_script_path = r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Ny mappe.ps1"

def tekst4():
    global current_script_path
    update_text("Åbner Word")
    current_script_path = r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Word.ps1"

def run_selected_script():
    # Brug den gemte sti til at køre det valgte script
    run_powershell_script(current_script_path)
    
# Opret vinduet
root = tk.Tk()
root.geometry('500x500')
root.title("Simpelt Tkinter eksempel")

# Opret tekstbox i højre side
text_box = tk.Text(root, width=40, height=10)
text_box.grid(row=0, column=1, rowspan=4, padx=10, pady=5)

# Opret frame om knapperne
frame = tk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(row=0, column=0, rowspan=6, padx=5, pady=5, sticky="ns")

# Opret knapper inde i frame
knap1 = tk.Button(frame, text="Backup", command=tekst1)
knap1.grid(row=0, column=0, padx=2, pady=5)
knap2 = tk.Button(frame, text="CMD", command=tekst2)
knap2.grid(row=1, column=0, padx=2, pady=5)
knap3 = tk.Button(frame, text="Ny mappe", command=tekst3)
knap3.grid(row=2, column=0, padx=2, pady=5)
knap4 = tk.Button(frame, text="Word", command=tekst4)
knap4.grid(row=3, column=0, padx=2, pady=5)
btn_close = tk.Button(frame, text="Luk vinduet", command=close_window)
btn_close.grid(row=4, column=0, padx=2, pady=5)

# Opret "Kør script" knappen under tekstboksen
btn_run_script = tk.Button(root, text="Kør script", command=run_selected_script)
btn_run_script.grid(row=4, column=1, padx=10, pady=5)

# Start Tkinter event loop
root.mainloop()



"""DUPES
button = tk.Button(root, text="Klik på mig", command=on_button_click)

button.grid(row=0, column=0, padx=2, pady=0)

def tekst1():
    update_text('tilføj tekst')
    run_powershell_script(r"indsæt sti")
"""