from tkinter import *
from tkinter import messagebox
import os
class GestorDeClientes:
    def __init__(self, root):      
        self.root = root
        self.root.title("Gestor de clientes")
        self.root.resizable(0, 0)
        self.root.geometry("800x800")
        self.root.config(bg="#D8BFD8")

        # CONTENEDOR PRINCIPAL (Padre)
        self.frame = Frame(self.root, bg="beige", bd=3)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=750, height=750)

        # ELEMENTOS / WIDGETS
        label = Label(self.frame, text="Gestor de Clientes", bg="#D8BFD8", fg="black", font="Arial 20 bold")
        label.pack(pady=20)

        # CAMPOS 
        field_frame1 = Frame(self.frame, bg="beige")
        field_frame1.pack(pady=10)
        label1 = Label(field_frame1, text="Nombre del cliente:", bg="beige", fg="black", font="Arial 15")
        label1.pack(side=LEFT, padx=5)
        self.entry1 = Entry(field_frame1, font="Arial 15")
        self.entry1.pack(side=LEFT, padx=5)

        field_frame2 = Frame(self.frame, bg="beige")
        field_frame2.pack(pady=10)
        label2 = Label(field_frame2, text="Telefono del cliente:", bg="beige", fg="black", font="Arial 15")
        label2.pack(side=LEFT, padx=5)
        self.entry2 = Entry(field_frame2, font="Arial 15")
        self.entry2.pack(side=LEFT, padx=5)

        field_frame3 = Frame(self.frame, bg="beige")
        field_frame3.pack(pady=10)
        label3 = Label(field_frame3, text="Correo del cliente:", bg="beige", fg="black", font="Arial 15")
        label3.pack(side=LEFT, padx=5)
        self.entry3 = Entry(field_frame3, font="Arial 15")
        self.entry3.pack(side=LEFT, padx=5)

        # Boton add
        button = Button(self.frame, text="Agregar cliente", bg="#D8BFD8", fg="black", font="Arial 15 bold", width=15, height=1, command=self.agregar_cliente)
        button.pack(pady=10)

        # Boton supr
        button1 = Button(self.frame, text="Eliminar cliente", bg="#D8BFD8", fg="black", font="Arial 15 bold", width=15, height=1, command=self.eliminar_cliente)
        button1.pack(pady=10)

        # Ventana CLIOENTES
        self.frameview = Frame(self.frame, bg="white", bd=3)
        self.frameview.pack(pady=20, fill=BOTH, expand=True)

        # Listbox LISTA
        self.listbox = Listbox(self.frameview, font="Arial 15", bg="white", fg="black")
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        # scrollbar
        scrollbar = Scrollbar(self.frameview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # scroll configg
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.cargar_clientes()



    def agregar_cliente(self):
        nombre = self.entry1.get()
        telefono = self.entry2.get()
        correo = self.entry3.get()
        
        if nombre and telefono and correo:
            cliente = f"Nombre: {nombre}, Teléfono: {telefono}, Correo: {correo}"
            
            self.listbox.insert(END, cliente)

            with open("clientes.txt", "a") as file:
                file.write(cliente + "\n")
            
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
        else:
            messagebox.showwarning("ERROR", "Por favor, complete todos los campos.")

    def eliminar_cliente(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            index = seleccion[0]
            self.listbox.delete(index)
            self.guardar_clientes()
        else:
            messagebox.showwarning("ERROR", "Por favor, seleccione un cliente para eliminar.")

    def cargar_clientes(self):
        if os.path.exists("clientes.txt"):
            with open("clientes.txt", "r") as file:
                for line in file:
                    cliente = line.strip()
                    self.listbox.insert(END, cliente)

    def guardar_clientes(self):
        with open("clientes.txt", "w") as file:
            for cliente in self.listbox.get(0, END):
                file.write(cliente + "\n")

if __name__ == "__main__":
    root = Tk()
    app = GestorDeClientes(root)
    root.mainloop()