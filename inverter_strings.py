string = 'Bob Esponja'
string_invertida = ''
indice = -1

while True:
    if len(string) == len(string_invertida):
        break
    letter = string[indice]
    string_invertida += letter
    indice -= 1
    
print(f'A string "{string}" invertida é: "{string_invertida}"')