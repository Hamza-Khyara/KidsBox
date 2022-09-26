import math


def main():
    B = int(input("Nombre abris: "))
    list_abris = []

    # remplissage liste abris
    for abri in range(B):
        #  l'entrée "params" doit être sous la forme: Identifiant X Y
        params = (input().split())
        abri_identifiant = params[0]
        abri_x = int(params[1])
        abri_y = int(params[2])

        list_abris.append((abri_identifiant, abri_x, abri_y))

    K = int(input("Nombre enfants: "))
    list_enfants = []

    # remplissage liste enfant
    for enfant in range(K):
        #  l'entrée "params" doit être sous la forme: Identifiant X Y
        params = (input().split())
        enfant_identifiant = params[0]
        enfant_x = int(params[1])
        enfant_y = int(params[2])

        list_enfants.append((enfant_identifiant, enfant_x, enfant_y))

    # Fonction anonyme pour calculer la distance entre l'enfant et abri
    dist_func = lambda x1, y1, x2, y2: math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    for enfant in list_enfants:
        abri_index = 0

        # Calculer la distance entre un enfant et le premier abri et supposez-le comme la distance la plus proche
        nearest_dist = dist_func(enfant[1], enfant[2], list_abris[abri_index][1], list_abris[abri_index][2])

        abri_counter = 1
        while abri_counter < len(list_abris):
            # Calculer la distance entre l'enfant et les autres abris
            new_dist = dist_func(enfant[1], enfant[2], list_abris[abri_counter][1], list_abris[abri_counter][2])

            # Comparez la nouvelle distance avec la distance la plus proche
            # si elle est inférieure à la distance la plus proche, attribuez-la à la distance la plus proche et enregistrez l'indice d'abri
            if new_dist < nearest_dist:
                nearest_dist = new_dist
                abri_index = abri_counter

            abri_counter += 1

        print(enfant[0], list_abris[abri_index][0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

