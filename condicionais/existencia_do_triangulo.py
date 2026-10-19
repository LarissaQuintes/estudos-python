lado1 = int(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = int(input("Digite o valor do segundo lado do triângulo: "))
lado3 = int(input("Digite o valor do terceiro lado do triângulo: "))

soma_lados_1_2 = lado1 + lado2
soma_lados_2_3 = lado2 + lado3
soma_lados_3_1 = lado3 + lado1

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("inválido")
elif lado1 >= soma_lados_2_3 or lado2 >= soma_lados_3_1 or lado3 >= soma_lados_1_2:
    print("não existe")
else:
    print("existe")