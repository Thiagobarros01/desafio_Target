#5) Escreva um programa que inverta os caracteres de um string.

caractere = str(input("Digite uma palavra: "))

invertida = ""

for i in range(len(caractere)-1,-1,-1):
    invertida += caractere[i]
    
print(invertida)