import tkinter as tk
from tkinter import messagebox
import subprocess
import os

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

def open_script_folder():
    if current_script_path:
        folder_path = os.path.dirname(current_script_path)
        try:
            os.startfile(folder_path)
        except Exception as e:
            messagebox.showerror("Fejl", f"Kunne ikke åbne mappen: {str(e)}")
    else:
        messagebox.showerror("Fejl", "Intet script valgt")

def select_script(event):
    global current_script_path
    selected_index = listbox.curselection()
    if selected_index:
        script_name = listbox.get(selected_index)
        for name, path in button_info:
            if name == script_name:
                update_text(f'Script: {name}')
                current_script_path = path
                break

def run_selected_script():
    # Brug den gemte sti til at køre det valgte script
    run_powershell_script(current_script_path)

# Opret vinduet
root = tk.Tk()
root.geometry('600x600')
root.title("Simpelt Tkinter eksempel")

# Opret tekstbox i højre side
text_box = tk.Text(root, width=40, height=10)
text_box.grid(row=0, column=1, rowspan=4, padx=10, pady=5)

# Opret et canvas med scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Placér canvas og scrollbar i layoutet
canvas.grid(row=0, column=0, rowspan=1, sticky="ns")
scrollbar.grid(row=0, column=0, sticky="ns")

# Liste over navne og tilhørende PowerShell-scripts
button_info = [
    ("Backup", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Backup script.ps1"),
    ("CMD", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\open cmd.ps1"),
    ("Ny mappe", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Ny mappe.ps1"),
    ("Word", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\Word.ps1"),
    ("Opret bruger", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\1_CREATE_USERS.ps1"),
    ("Filer til VM", r"C:\Users\Morten M. Hansen\Desktop\Powerscripts\FiletoVM.ps1"),
]

# Sortér navne alfabetisk for listbox
button_info.sort(key=lambda x: x[0])

# Opret en Listbox i det scrollbare frame
listbox = tk.Listbox(scrollable_frame)
for name, path in button_info:
    listbox.insert(tk.END, name)
listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Bind Listbox selection til funktionen
listbox.bind('<<ListboxSelect>>', select_script)

# Opret "Kør script" knappen under tekstboksen
btn_run_script = tk.Button(root, text="Kør script", command=run_selected_script)
btn_run_script.grid(row=4, column=1, padx=10, pady=5)

# Opret "Åbn mappe" knappen
btn_open_folder = tk.Button(root, text="Åbn mappe", command=open_script_folder)
btn_open_folder.grid(row=5, column=1, padx=10, pady=5)

# Start Tkinter event loop
root.mainloop()
