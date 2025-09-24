import re

try:
    altura_input = input("Digite a altura do andar (ex: 3.5m): ")
    altura = float(re.sub(r"[^\d.]", "", altura_input))  # Remove tudo que não for número ou ponto
    andares = float(input("Digite a quantidade de andares (ex: 10): "))
    print(f"A altura total do prédio é de {altura * andares} metros.")
except ValueError:
    print("Digite apenas números válidos.")