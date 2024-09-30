# importamos la libreria Tkinter
from tkinter import *
from tkinter import ttk

#creación de ventana
ventana =Tk()
ventana.geometry ("500x500")


ventana.title ("Sistema de gestion de ventas")
ventana.resizable(0,0)

# Menu de inicio
def home():

    # Montar pantalla
    home_label.config(
        fg="white", 
        bg="black",
        font=("Arial",30),
        padx=210,
        pady=20,
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)
    
    # Borrar la lista de productos anterior y evitar que se dupliquen
    products_box.delete(*products_box.get_children())  
    
    # Listar los productos 
    for product in products:
        products_box.insert('', 0, text=product[0], values=(product[1], product[3]))
    
    # Ocultar pantalla
    add_label.grid_remove()
    info_label.grid_remove()
    add_name_label.grid_remove()
    add_price_label.grid_remove()
    add_description_label.grid_remove()
    add_quantity_label.grid_remove()
    add_separator.grid_remove()
    boton.grid_remove()
    info_table.grid_remove()
    return True

# Menu de Agregar
def add():
    
    add_label.config(
        fg="white", 
        bg="red",
        font=("Arial",30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    #campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    add_quantity_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_quantity_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    
    add_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("consolas",12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)
    boton.grid(row=6, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    # ocultar pantalla
    home_label.grid_remove()
    info_label.grid_remove()
    products_box.grid_remove()
    info_table.grid_remove()
    return True

# Menu de informacion
def info():
    
    info_label.config(
        fg="white", 
        bg="blue",
        font=("Arial",30),
        padx=160,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    # Mostrar tabla
    info_table.grid(row=1, column=0, columnspan=4)
    
    info_table.delete(*info_table.get_children()) 
    
    # Agregar información de productos a la tabla
    for product in products:
        info_table.insert('', 'end', text=product[0], values=(product[3], product[1], product[2]))
    
    # Ocultar pantalla
    add_label.grid_remove()
    home_label.grid_remove()
    add_name_label.grid_remove()
    add_name_label.grid_remove()
    add_price_label.grid_remove()
    add_description_label.grid_remove()
    add_quantity_label.grid_remove()
    products_box.grid_remove()
    
    return True

# Añadir datos a una lista
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        quantity_data.get(),
        add_description_entry.get("1.0", "end-1c")
         
    ])

    # Borrar los datos del formulario
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    quantity_data.set("")  # Borrar el valor de quantity_data

    add()

# Variables importantes
name_data=StringVar()
price_data=StringVar()
quantity_data=StringVar()
products=[]

#Definir campos de pantalla
info_label = Label(ventana, text="Información")
home_label = Label(ventana, text="Ventas")

# Datos de pantalla de Inicio
Label(ventana).grid(row=1)
products_box=ttk.Treeview(height=12,columns=('Precio', 'Cantidad'))
products_box.column("#0", anchor=W, width=200)  # Ajustar ancho de la columna de texto
products_box.column("#1", anchor=W, width=150)  # Ajustar ancho de la columna de precio
products_box.column("#2", anchor=W, width=85)  # Ajustar ancho de la columna de cantidad
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)
products_box.heading("#2", text='Cantidad', anchor=W)

#Campos del formulario
add_name_label = Label (ventana, text="Nombre del producto:")
add_name_entry=Entry(ventana, textvariable=name_data)

add_price_label = Label (ventana, text="Precio del producto:")
add_price_entry=Entry(ventana, textvariable=price_data)

add_quantity_label= Label (ventana, text="Cantidad:")
add_quantity_entry=Entry(ventana, textvariable=quantity_data)

add_description_label= Label (ventana, text="Descripcion:")
add_description_entry= Text(ventana)

add_label = Label (ventana, text="Añadir producto")

add_separator=Label(ventana)
boton=Button(ventana, text="GUARDAR", command=add_product)

# Crear tabla para mostrar información de productos
Label(ventana).grid(row=1)
info_table = ttk.Treeview(height=12, columns=('Producto', 'Cantidad', 'Precio', 'Descripcion'))
info_table.column("#0", anchor=W, width=100)  # Ajustar ancho de la columna de cantidad
info_table.column("#1", anchor=W, width=65)  # Ajustar ancho de la columna de producto
info_table.column("#2", anchor=W, width=85)  # Ajustar ancho de la columna de precio
info_table.column("#3", anchor=W, width=200)  # Ajustar ancho de la columna de descripción
info_table.heading("#0", text='Producto', anchor=W)
info_table.heading("#1", text='Cantidad', anchor=W)
info_table.heading("#2", text='Precio', anchor=W)
info_table.heading("#3", text='Descripcion', anchor=W)

#llamada a la función
add()

# Creación de Menu
menu_superior=Menu(ventana)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Ventas", command=home)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
ventana.config (menu=menu_superior)

#visualización de la ventana
ventana.mainloop()