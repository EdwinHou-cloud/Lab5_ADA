# Importamos la librería Tkinter y ttk para la interfaz gráfica
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Creación de la ventana principal
ventana =Tk()
ventana.geometry ("500x500") # Establece el tamaño de la ventana
ventana.title ("Sistema de gestion de ventas") # Título de la ventana
ventana.resizable(0,0) # Evita que se pueda cambiar el tamaño de la ventana

# Función para mostrar el menú de ventas
def sales():

    # Muestra la pantalla de ventas con un título
    sales_label.config(
        fg="white", 
        bg="black",
        font=("Arial",30),
        padx=187,
        pady=20,
    )
    sales_label.grid(row=0, column=0, columnspan=4)

    # Muestra la lista de productos
    products_box.grid(row=1, column=0)
    
    # Borra la lista de productos anterior y evita que se dupliquen
    products_box.delete(*products_box.get_children())  
    
    # Lista los productos en la tabla de ventas
    for product in products:
        products_box.insert('', 0, text=product[0], values=(product[1], product[2]))
    
    # Oculta pantalla de otros menús
    add_label.grid_remove()
    add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_description_label.grid_remove()
    add_description_entry.grid_remove()
    add_quantity_label.grid_remove()
    add_quantity_entry.grid_remove()
    add_separator.grid_remove()
    boton.grid_remove()
    info_label.grid_remove()
    info_table.grid_remove()
    total_label.grid_remove()
    return True

# Función para mostrar el menú de agregar productos
def add():
    
    # Muestra la pantalla de agregar productos con un título
    add_label.config(
        fg="white", 
        bg="red",
        font=("Arial",30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    # Muestra los campos del formulario para agregar un producto
    add_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    
    add_quantity_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    add_quantity_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    
    add_description_label.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("consolas",12),
        padx=15,
        pady=15
    )

    # Muestra botón de guardar y un separador
    add_separator.grid(row=6)
    boton.grid(row=6, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    # Oculta las pantallas de otros menús
    sales_label.grid_remove()
    info_label.grid_remove()
    products_box.grid_remove()
    info_table.grid_remove()
    total_label.grid_remove()
    return True

# Función para mostrar el menú de información de productos
def info():
    info_label.config(
        fg="white", 
        bg="blue",
        font=("Arial",30),
        padx=146,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    # Muestra la pantalla de información con un título
    info_table.grid(row=1, column=0)
    info_table.delete(*info_table.get_children()) 
    
    # Agrega información detallada de los productos
    for product in products:
        info_table.insert('', 'end', text=product[0], values=(product[2], product[1], product[3]))
        
    # Calcula y muestra total de ventas del día
    calculate_total_sales()
    total_label.grid(row=2, column=0)  
    
    # Oculta las pantallas de otros menús
    add_label.grid_remove()
    add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_description_label.grid_remove()
    add_description_entry.grid_remove()
    add_quantity_label.grid_remove()
    add_quantity_entry.grid_remove()
    add_separator.grid_remove()
    boton.grid_remove()
    sales_label.grid_remove()
    products_box.grid_remove()
    return True

# Función para calcular el total de ventas del día
def calculate_total_sales():
    total = 0
    # Recorre los productos y sumar el precio total
    for product in products:
        price = float(product[1])  # Convierte el precio a float
        quantity = int(product[2])  # Convierte la cantidad a int
        total += price * quantity   # Suma el precio * cantidad al total

    # Muestra el total en la pantalla
    total_label.config(text=f"Total ventas del día: ${total:.2f}")
    total_label.grid(row=2, column=0)
    
    
# Función para agregar un nuevo producto a la lista
def add_product():
    
    #llamada a funcion para la verificacion de los campos ingresados
    precio = es_precio(price_data.get())
    if precio is None:
        return

    cantidad = es_cantidad(quantity_data.get())
    if cantidad is None:
        return
    
    # Añade los datos del formulario a la lista de productos
    products.append([
        name_data.get(),
        price_data.get(),
        quantity_data.get(),
        add_description_entry.get("1.0", "end-1c") # Captura descripción del producto
         
    ])

    # Limpia los campos del formulario después de agregar
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    quantity_data.set("")  # Borra el valor de quantity_data

    # Vuelve a mostrar el formulario de agregar productos
    add()

#Verificar si el precio ingresado es un numero 
def es_precio(precio):
    try:
        return float(precio)
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un valor numérico.")
        return None

#Verificar si la cantidad ingresada es un entero
def es_cantidad(cantidad):
    try:
        cantidad_int = int(cantidad)
        if cantidad_int < 0:
            raise ValueError
        return cantidad_int
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero mayor o igual a 0.")
        return None

# Se definen las variables para almacenar datos del formulario
name_data=StringVar()
price_data=StringVar()
quantity_data=StringVar()
total_label = Label(ventana, text="", font=("Arial", 12)) # Etiqueta para mostrar el total
products=[] # Lista de productos

# Crea etiquetas para los distintos menús
info_label = Label(ventana, text="Información")
sales_label = Label(ventana, text="Ventas")

# Datos de pantalla de Ventas
Label(ventana).grid(row=1)
products_box=ttk.Treeview(height=12,columns=('Precio', 'Cantidad'))
products_box.column("#0", anchor=W, width=225)  # Ajusta el ancho de la columna de texto
products_box.column("#1", anchor=W, width=175)  # Ajusta el ancho de la columna de precio
products_box.column("#2", anchor=W, width=98)  # Ajusta el ancho de la columna de cantidad
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
info_table = ttk.Treeview(height=12, columns=('Cantidad', 'Precio', 'Descripcion'))
info_table.column("#0", anchor=W, width=110)  # Ajusta el ancho de la columna de cantidad
info_table.column("#1", anchor=W, width=65)  # Ajusta el ancho de la columna de producto
info_table.column("#2", anchor=W, width=95)  # Ajusta el ancho de la columna de precio
info_table.column("#3", anchor=W, width=228)  # Ajusta el ancho de la columna de descripción
info_table.heading("#0", text='Producto', anchor=W)
info_table.heading("#1", text='Cantidad', anchor=W)
info_table.heading("#2", text='Precio', anchor=W)
info_table.heading("#3", text='Descripcion', anchor=W)

# Mostrar el menú de agregar productos al iniciar
add()

# Crea el menú superior
menu_superior=Menu(ventana)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Ventas", command=sales)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)
ventana.config (menu=menu_superior)

# Visualización de la ventana principal
ventana.mainloop()