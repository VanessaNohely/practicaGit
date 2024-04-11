# Funcion Tabla
def tabla(numero):
    for x in range(1,11):
        print(f"{numero} x {x} = {numero*x}")

# Prueba de funcion tabla
print("Prueba funcion tabla:")
tabla(9)

#Funcion operaciones
def operaciones(operacion,num1,num2):
    if operacion == "suma":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operacion == "resta":
        print(f"{num1} - {num2} = {num1-num2}")
    elif operacion == "multiplicacion":
        print(f"{num1} x {num2} = {num1*num2}")
    elif operacion == "division":
        print(f"{num1} / {num2} = {num1/num2}")

#prueba operaciones
print("Prueba funcion operaciones:")
operaciones("suma",5,6)
operaciones("resta",7,9)
operaciones("multiplicacion",4,6)
operaciones("division",4,6)