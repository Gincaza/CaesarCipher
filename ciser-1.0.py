#This file only modifys files that have strings, it doesn't crypt any binary file.

import argparse
import os

Letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

files = []

for file in os.listdir():
    if not file.endswith(".py"):
        if os.path.isfile(file):
            files.append(file)

def main():
    parser = argparse.ArgumentParser(description='Codificador ou Decodificador com a criptografia Caesar Cipher')
    parser.add_argument('-D', action='store_true', help='Ativar modo decrypt')

    args = parser.parse_args()

    if args.D:
        for file in files:
            with open(file, "r") as thefile:
                contents = thefile.read()
            
            frase1 = Decode(contents)
            with open(file, "w") as thefile:
                thefile.write(frase1)
    else:
        for file in files:
            with open(file, "r") as thefile:
                contents = thefile.read()
            
            frase1 = Cisex(contents)  
            with open(file, "w") as thefile:
                thefile.write(frase1)

def Cisex(valor0):
    print("[+] Coding...")
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

def Decode(valor0):
    valor1 = valor0.upper() 
    string = ''
    for c in valor1:
        if c in Letras:
            num = Letras[c]

            result = (num - 3) % 26
            for chave, valor in Letras.items():
                if valor == result:
                    string += chave
        else:
            string += c
    return string

if __name__ == "__main__":
    main()
