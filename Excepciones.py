# Un ejemplo de error
# print(1/0) 0-9

numero_var = "hola"

try:
    print(int(numero_var))
except Exception as error :
    print(f" El valor que se recibe no es tipo entero {error}")

print("Hola Mundo")

def ejemplo():
    return

ejemplo()

for a in range(10):
    print(2)
else:
    pass