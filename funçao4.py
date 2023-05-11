print("O Rato roeu a roupa do rei de Roma")

def conta_vogais(string):
    string = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += string.count(i)
    return result

print("essa frase tem",conta_vogais('O rato roeu a roupa do rei de roma'),"vogais")


"""def vogais(t):
    cont=0
    for x in t:
        if x in "aeiouAEIOU":
            cont += 1
    print(cont)
texto="O Rato roeu a roupa do rei de roma"
vogais(texto)
"""