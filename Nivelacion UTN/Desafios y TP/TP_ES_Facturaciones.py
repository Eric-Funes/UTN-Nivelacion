#Enunciado:Para el departamento de facturación:
#A. Ingresar tres precios de productos y mostrar la suma de los mismos.
pto1= float(input("Ingresa el precio de un producto: "))
pto2= float(input("Ingresa el precio de un producto: "))
pto3= float(input("Ingresa el precio de un producto: "))
print("\n El precio final de la compra seria:", pto1 + pto2 + pto3)


#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
pto1= float(input("\nIngresa el precio de un producto: "))
pto2= float(input("Ingresa el precio de un producto: "))
pto3= float(input("Ingresa el precio de un producto: "))
print("\n El precio promedio de los productos seria:", (pto1 + pto2 + pto3)/3)


#C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
pto1= float(input("\nIngresa el precio de un producto: "))
pto2= float(input("Ingresa el precio de un producto: "))
pto3= float(input("Ingresa el precio de un producto: "))
precio_final= (pto1 + pto2 + pto3)
print("\n El precio final de la compra incluyendo IVA seria:", precio_final*1.21)

#La variable precio_final ni si quiera hace falta, se puede poner esa suma directo en el print final