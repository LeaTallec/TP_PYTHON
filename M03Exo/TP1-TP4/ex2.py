# créez une fonction qui prend en paramètre une suite de longueur indéterminée de int
# et qui renvoi la valeur en bit de la multiplication de ceux ci

def multiply_to_binary(*integers):
    total = 1
    for integer in integers:
        total *= integer
    return bin(total)

resultat = multiply_to_binary(3, 2, 3)

print(f"Le résultat est : {resultat}")