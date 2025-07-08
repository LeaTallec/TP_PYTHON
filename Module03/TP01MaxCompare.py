def max(var1, var2):
    if var1 < var2:
        return var2
    else:
        return var1

def compare(var1, var2):
    egale = 0
    var1_superieur = 1
    var2_superieur = -1

    if var1 == var2:
        return egale
    elif var1 > var2:
        return var1_superieur
    else:
        return var2_superieur

def max_compare(var1, var2):
    max1 = max(var1, var2)
    comp1 = compare(var1, var2)

    print("La valeur la plus grande est :", max1)
    print("La valeur est :", comp1)

valeur1 = int(input("Entrer la valeur de la piece 1 : "))
valeur2 = int(input("Entrer la valeur de la piece 2 : "))
max_compare(valeur1, valeur2)