from package.storage import LeituraCodigoBarras



from tkinter import messagebox
import tkinter as tk
import json
import subprocess



class GUI:

    def __init__(self, master):
    
        self.master = master
        self.master.title("Leitor de Código de Barras")
        self.master.geometry("520x300")

        master.grid_columnconfigure(1, minsize=400)

        tk.Label(master, text="Código de Barras:").grid(row=0, sticky='w')
        tk.Label(master, text="Descrição:").grid(row=1, sticky='w')
        tk.Label(master, text="Parceiro:").grid(row=2, sticky='w')
        tk.Label(master, text="Preço:").grid(row=3, sticky='w')
        tk.Label(master, text="Status:").grid(row=4, sticky='w')

        self.code_entry = tk.Entry(master)
        self.code_entry.grid(row=0, column=1, sticky='ew')
        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=1, column=1, sticky='ew')
        self.partner_entry = tk.Entry(master)
        self.partner_entry.grid(row=2, column=1, sticky='ew')
        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=3, column=1, sticky='ew')
        self.status_entry = tk.Entry(master)
        self.status_entry.grid(row=4, column=1, sticky='ew')

        self.load_button = tk.Button(master, text="LOAD", command=self.load_data)
        self.load_button.grid(row=5, column=0, columnspan=2, sticky='ew')
        self.stop_button = tk.Button(master, text="STOP", command=self.stop_program)
        self.stop_button.grid(row=6, column=0, columnspan=2, sticky='ew')
        self.new_product_button = tk.Button(master, text="NEW_PRODUCT", command=self.new_product)
        self.new_product_button.grid(row=7, column=0, columnspan=2, sticky='ew')
        self.clearall_button = tk.Button(master, text="CLEAR ALL", command=self.clear_all)
        self.clearall_button.grid(row=8, column=0, columnspan=2, sticky='ew')

        self.controller = LeituraCodigoBarras()


    def load_data(self):
        if self.controller.products:
            for product in self.controller.products:
                product.show()
        else:
            print("Nenhum produto encontrado.")


    def stop_program(self):
        self.master.quit()


    def new_product(self):
        code = self.code_entry.get()
        description = self.description_entry.get()
        partner = self.partner_entry.get()
        price = self.price_entry.get()
        status = self.status_entry.get()

        if code and description and partner and price and status:
            self.controller.insertProduct(code, description, partner, price, status)
            self.controller.record()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def clear_all(self):
        self.code_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.partner_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
        self.controller.clear_terminal()



#################################################################################


class Monitor:
    

    def __init__(self):
        self.root = tk.Tk()
        self.app = GUI(self.root)
    

    def iniciar(self):
        self.root.mainloop()


