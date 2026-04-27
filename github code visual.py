"""hola equipoo"""
rango = int(input("ingresar cantidad de veces que desea comprar: "))
for i in range(rango):
    ventas= [rango]
    monto= float(input("Ingrese el monto de sus productos"))
    ventas.append(monto)
    array+= monto
    print("la suma de la compra de sus productos es de: $",array)