import math

def verifica_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

def calcula_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if verifica_triangulo(a, b, c):
    area = calcula_area(a, b, c)
    print(f"A área do triângulo é {area:.2f}")
else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")
