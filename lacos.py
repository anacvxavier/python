"""
soma = 0
n = int(input("Digite um número inteiro ou 0 para sair: "))

while n != 0:
    soma+= n
    n = int(input("Digite um número inteiro ou 0 para sair: "))

print("Total: ", soma)

"""

"""
maior = -1
n = int(input("Digite um número positivo e inteiro: "))

while n >= 0:
    if n > maior:
        maior = n
    n = int(input("Digite um número positivo e inteiro: "))
print("Maior número:", maior)
"""

x, y = 5, 15

while x < 10 and y > 15:
    print(f"x = {x}, y = {y}")
    x+=1
    y-=1
print("Loop concluído")
print(f"Valores finais de x: {x} e y: {y}")