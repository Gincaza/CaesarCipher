#This file is only for cryption action

Letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}



def Cisex(valor0):
    valor1 = valor0.upper() 
    string = ''
    for c in valor1:
        if c in Letras:
            num = Letras[c]

            result = (num + 3) % 26
            for chave, valor in Letras.items():
                if valor == result:
                    string += chave
        else:
            string += c
    return string


frase = input('Frase: ')
frase1 = Cisex(frase)
print(frase1)




