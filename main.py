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
                # Vis indholdet af scriptet i tekstboksen
                try:
                    with open(path, 'r') as file:
                        script_content = file.read()
                        update_text(script_content)
                except Exception as e:
                    messagebox.showerror("Fejl", f"Kunne ikke læse scriptfilen: {str(e)}")
                
                # Opdater den globale scriptsti
                current_script_path = path
                break

def run_selected_script():
    # Brug den gemte sti til at køre det valgte script
    run_powershell_script(current_script_path)

# Opret vinduet
root = tk.Tk()
root.geometry('800x600')  # Øg vinduets størrelse for bedre visning
root.title("Simpelt Tkinter eksempel")

# Sæt baggrundsfarve til lyseblå
root.configure(bg='#ADD8E6')  # Lyseblå farvekode

# Hent skærmstørrelse
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Beregn ønsket størrelse til tekstboksen
text_box_width = int(screen_width * 0.25)  # 25% af skærmens bredde
text_box_height = int(screen_height * 0.25)  # 25% af skærmens højde

# Opret tekstbox i højre side
text_box = tk.Text(root, width=text_box_width // 10, height=text_box_height // 20)  # Juster dimensioner
text_box.grid(row=0, column=1, rowspan=3, padx=10, pady=5, sticky="nsew")

# Opret en Frame til listbox og scrollbar
listbox_frame = tk.Frame(root, bg='#ADD8E6')  # Lyseblå baggrundsfarve
listbox_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=5, sticky="ns")

# Opret et canvas med scrollbar
canvas = tk.Canvas(listbox_frame, bg='#ADD8E6', highlightthickness=0)  # Lyseblå baggrundsfarve og ingen kantlinje
scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg='#ADD8E6')  # Lyseblå baggrundsfarve

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Placér canvas og scrollbar i listbox_frame
canvas.grid(row=0, column=0, sticky="ns")
scrollbar.grid(row=0, column=1, sticky="ns")


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

# Opret knapperne under tekstboksen
button_frame = tk.Frame(root, bg='#ADD8E6')  # Lyseblå baggrundsfarve
button_frame.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Opret "Kør script" knappen
btn_run_script = tk.Button(button_frame, text="Kør script", command=run_selected_script)
btn_run_script.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Opret "Åbn mappe" knappen
btn_open_folder = tk.Button(button_frame, text="Åbn mappe", command=open_script_folder)
btn_open_folder.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Juster kolonne- og rækkevægte for at få elementerne til at skalere korrekt
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start Tkinter event loop
root.mainloop()
