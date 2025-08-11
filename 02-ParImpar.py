print("Hola, bienvenido a mi tercer ejercio en Python")
print()
print("si un numero es par o impar")
print()
n1 = int(input("ingrese el numero que desea comprobar"))

if n1 % 2 ==0  :
    print(f"el numero, {n1} es par")
elif n1 < 0 : 
    print("debe ingresar un numero entro positivo")
else:
    print(f"el numero, {n1} es impar")
print()
print("Gracias por participar")