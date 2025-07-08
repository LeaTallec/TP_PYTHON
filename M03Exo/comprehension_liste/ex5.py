# crée une liste de liste
# pour les tables de multiplications de 1 à 10
# [[1,2,3,...], [2,4,6,...],...]

table_multiplication = [[x*y for y in range(1, 11)] for x in range(1, 11)]
print(table_multiplication)