#Pizzas DUOC UC

import json
from datetime import datetime

ventas =[]
#diccionario
precios_pizzas = {
    "cuatro quesos": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "hawaiana": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "napolitana": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},
    "pepperoni": {"pequeña": 7000, "mediana": 10000, "familiar": 13000},
}
def menu():
    print("\n--- Sistema de ventas de Pizzas DUOC UC---")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar ventas por cliente")
    print("4. Guardar las ventas en un archivo")
    print("5. Cargar las ventas desde un archivo.")
    print("6. Generar Boleta")
    print("7. Anular venta.")
    print("8. Salir del programa.")
    
def registrar_venta():
    nombre_cliente = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente(diurno, vespertino o administrativo): ").lower()
    tipo_pizza = input("Tipo de pizza(cuatro quesos, hawaiana, napolitana o pepperoni): ").lower()
    tamaño_pizza = input("tamaño de la pizza(pequeña, mediana o familiar): ").lower()
    cantidad = int(input("Cuantas pizzas desea: "))

    precio_unitario =precios_pizzas[tipo_pizza][tamaño_pizza]
    
    descuento=0
    
    if tipo_cliente=='diurno':
        descuento = 0.88
    elif tipo_cliente == 'vespertino':
        descuento = 0.86
    elif tipo_cliente == 'administrativo':
        descuento = 0.9
       
    precio_total = precio_unitario * cantidad
    precio_final =precio_total*descuento
    descuentos = precio_total - precio_final
    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    venta={
        "Fecha_hora": fecha_hora,
        "Cliente":nombre_cliente,
        "tipo de cliente": tipo_cliente,
        "Tipo de pizza": tipo_pizza,
        "Tamaño": tamaño_pizza,
        "Cantidad": cantidad,
        "Precio_total": precio_total,
        "Descuento": descuentos,
        "Total_a_pagar": precio_final
    }
    ventas.append(venta)
    
def mostrar_ventas():
    for venta in ventas:
        print(venta)

def buscar_ventas():
    nombre_cliente = input("Nombre del cliente")
    for venta in ventas:
        if venta["Cliente"]==nombre_cliente:
            print(venta)

def guardar_ventas():
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo)
        print("Ventas guardadas")
        
def cargar_ventas():
    with open("ventas.json", "r") as archivo:
        ventas.clear()
        ventas.extend(json.load(archivo))
        print("Ventas cargadas")
        
def anular_venta():
    nombre_cliente = input("Ingrese el nombre del cliente de la venta que desea anular: ")
    for venta in ventas:
        if venta["Cliente"]== nombre_cliente:
            ventas.remove(venta)
            print("Venta anulada")
            return
    print("Venta no encontrada")
    
def generar_boleta():
    nombre_cliente = input("Nombre del cliente")
    for venta in ventas:
        if venta["Cliente"]==nombre_cliente:
            print("\t\tPizzas DUOC UC")
            print("-------------------------------")
            print("Fecha y hora:",      venta["Fecha_hora"])
            print("Cliente:",           venta["Cliente"])
            print("Tipo de cliente:",   venta["tipo de cliente"])
            print("Tipo de pizza:",     venta["Tipo de pizza"])
            print("Tamaño:",            venta["Tamaño"])
            print("Cantidad:",          venta["Cantidad"])
            print("-------------------------------")
            print("subtotal: $",        venta['Precio_total'])
            print("Descuento: $",       venta['Descuento'])
            print("Total a pagar: $",   venta['Total_a_pagar'])
            print("gracias por su compra")
            
while True:
    print(menu())
    op =int(input ("Seleccione una opción: "))


    if op == 1:
        registrar_venta()

    elif op == 2:
        mostrar_ventas()
    
    elif op == 3:
        buscar_ventas()
    
    elif op == 4:
        guardar_ventas()   
    
    elif op == 5:
        cargar_ventas()
    
    elif op == 6:
        generar_boleta()
    
    elif op == 7:
        anular_venta()
        
    elif op == 8: 
        print("Adios")
        break