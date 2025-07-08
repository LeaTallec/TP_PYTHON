# Pour un logiciel de gestion rh d'une agence d'interim
# complétez la fonction suivante sui calcule le salaire journalier
# d'un intérimaire
# après 8 heures de travail, les heures sont majorées de 25%, après 11heures de 50%

def calcul_salaire_journalier(nb_heures, taux_horaire):
    heures_normales = 8
    heures_majoration_25 = 8
    seuil_majoration = 11

    taux_majoration_25 = 1.25
    taux_majoration_50 = 1.5

    if nb_heures <= heures_normales:
        salaire = taux_horaire * nb_heures
    elif nb_heures <= 11:
        heures_majorees_25 = nb_heures - heures_majoration_25
        salaire = (
                (heures_normales * taux_horaire) +
                (heures_majorees_25 * taux_horaire * taux_majoration_25)
        )
    else:
        heures_majorees_25 = 3
        heures_majorees_50 = nb_heures - seuil_majoration
        salaire = (
            (heures_normales * taux_horaire) +
            (heures_majorees_25 * taux_horaire * taux_majoration_25) +
            (heures_majorees_50 * taux_horaire * taux_majoration_50)
        )

    return round(salaire, 2)

print(calcul_salaire_journalier(9, 10))
