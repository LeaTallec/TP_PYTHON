def echiquier_sissa():
    total = 0
    grains = 1

    for row in range(1, 9):
        print(f"===== Ligne : {row} =====")
        for col in range(1, 9):
            print(f"Colonne {col} : {grains:_} grains".replace("_", " "))
            total += grains
            grains *= 2

    print("==========")
    print(f"Total de grains de riz : {total:_} grains".replace("_", " "))

echiquier_sissa()