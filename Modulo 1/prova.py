# #Atividade número 1
# print("Conversor de temperaturas")
# print("1. Celsius para Fahrenheit")
# print("2. Fahrenheit para Celsius")

# number = int(input("Escolha uma opção:"))

# if number == 1:
#     c = float(input("Temperatura em celsius: "))
#     calc = ( c * 9 / 5) + 32
#     print(f"A conversão de {c}° C para fahrenheit é {calc:.1f}° F.")
# elif number == 2:
#     f = float(input("Temperatura em fahrenheit: "))
#     calc2 = ( f - 32) * 5 / 9
#     print(f"A conversão de {f}° F para celsius é {calc2:.1f}° C.")

# #Atividade número 2
# temperaturas = [28.5, 29.1, 27.3, 25.4, 23.9, 22.7, 22.1, 23.5, 24.6, 26.8, 27.9, 28.8]

# a = min(temperaturas)
# b = max(temperaturas)
# c = sum(temperaturas) / 12

# print(f"A menor temperatura é: {a}")
# print(f"A maior temperatura é: {b}")
# print(f"A média das temperaturas é: {c:.2f}")

# #Atividade número 3

# def menu():
#     print("Menu \n" 
#         "A - Criar estoque.\n" 
#         "B - Adicionar itens utilizando o nome do item e a quantidade.\n" \
#         "C - Consultar um item, utilizando o nome do produto.\n" \
#         "D - Atualizar a quantidade em estoque de um item.\n" \
#         "E - Exibir o estoque final.\n" \
#         "F - Sair do programa.")

# estoque = {}
# running = True

# while running:
#     menu()
#     n = str(input("Escolha a sua opção: "))
#     if n == "A" or n == "a":
#         estoque = {}
#         print("Você criou um estoque.")
#     elif n == "B" or n == "b":
#         nome = str(input("Adicione o item: "))
#         qntd = int(input("A quantidade do item: "))
#         estoque[nome] = qntd
#         print(estoque[nome])
#     elif n == "C" or n == "c":
#         consultar = str(input("Item que você procura: "))
#         item = estoque[consultar]
#         print(item)
#     elif n == "D" or n == "d":
#         conteudo = str(input("Item que deseja alterar quantidade: "))
#         mudar = str(input("Quantidade do item: "))
#         estoque[conteudo] = mudar
#         print(estoque[conteudo])
#     elif n == "E" or n == "e":
#         print(estoque)
#     elif n == "F" or "f":
#         print("Você saiu do programa.")
#         break 
#     else:
#         print("Essa opção não existe. Tente novamente.")

# #Atividade 4
# def converter_medidas():
#     n = str(input("Celsius ou Fanhrenheit: "))
#     m = float(input("Valor a ser convertido: "))
    
#     if n == "Celsius" or n == "celsius":
#         calc = ( m * 9 / 5) + 32
#         print(f"O valor de {m}° C convertido para Fanhrenheit é {calc:.1f}° F.")

#     elif n == "Fanhrenheit" or n == "fanhrenheit":
#         calc1 = ( m - 32) * 5 / 9
#         print(f"O valor de {m}° F convertido para Fanhrenheit é {calc1:.1f}° C ")

# converter_medidas()