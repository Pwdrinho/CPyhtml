import tkinter as tk
import psutil

root = tk.Tk()
root.overrideredirect(True) 
root.configure(bg="lightblue")
root.config(highlightthickness=3, highlightbackground="white", highlightcolor="white")
largura, altura = 320, 150
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

topbar = tk.Frame(root, bg="lightblue")
topbar.pack(fill="x")

def fechar():
    root.destroy()

btn_fechar = tk.Button(
    topbar, text="X", font=("Helvetica", 11),
    command=fechar, bg="red", fg="white",
    bd=0, activebackground="darkred", relief="flat"
)
btn_fechar.pack(side="left", padx=4, pady=4)

label = tk.Label(root, font=("Helvetica", 25), fg="Black", justify="left", bg="lightblue")
label.pack(expand=True)

def update_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    label.config(text=f"CPU Usage: {cpu}% \nRAM Usage: {ram}%")
    root.after(1000, update_stats)

update_stats()

def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

topbar.bind("<Button-1>", start_move)
topbar.bind("<B1-Motion>", do_move)

root.mainloop()