"""hola equipoo"""
array = 0
rango = int(input("ingresar cantidad de veces que desea comprar: "))
for i in range(rango):
    ventas= [rango]
    monto= float(input(f"Ingrese el monto del producto numero {i+1}:$"))
    ventas.append(monto)
    array+= monto
    print("la suma de la compra de sus productos es de: $",array)