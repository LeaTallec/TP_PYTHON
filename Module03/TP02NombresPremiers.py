def nombre_premier(n) :
    for i in range(2,int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True

limite = int(input("Entrez la limite supérieure : "))

for nombre in range(limite + 1):
    if nombre_premier(nombre):
        print(nombre)