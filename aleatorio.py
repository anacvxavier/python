import random


numero_secreto = (random.randint(1, 10))
#print(numero_secreto)
chute = int(input("Tente adivinhar o número secreto entre 1 e 10: "))

if chute == numero_secreto:
    
    # Se o usuário adivinhar corretamente, imprime uma mensagem de sucesso
    print("Parabéns! Você adivinhou o número secreto.")

else:
    
    # Se o usuário adivinhar errado, imprime uma mensagem de erro
    print("Desculpe, você não adivinhou o número secreto. Tente novamente!")