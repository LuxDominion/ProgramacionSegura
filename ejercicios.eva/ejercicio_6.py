alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfabeto), 1, -1):  # range(valor_inicio, valor_fin, avance)
    if i % 2 == 0:
        alfabeto.pop(i-1)
print(alfabeto)
