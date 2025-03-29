# Fonction pour afficher une image sous forme de caractères
def AfficheImage(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 0:
                print("0", end=" ")  # Pixel noir
            else:
                print(" ", end=" ")  # Pixel blanc (espace)
        print()  # Nouvelle ligne après chaque ligne de l'image
    print("---")  # Séparateur pour plus de clarté

# Fonction pour vérifier et corriger la symétrie verticale
def VerifSymetrieVerif(tab):
    n = len(tab)  # Nombre de lignes
    m = len(tab[0])  # Nombre de colonnes
    symetrique = True  # Variable pour vérifier si l'image est symétrique

    # Vérifier la symétrie verticale
    for i in range(n):
        for j in range(m // 2):  # On parcourt jusqu'à la moitié de l'image
            if tab[i][j] != tab[i][m-1-j]:  # Comparer les pixels symétriques
                symetrique = False
                break

    # Si l'image n'est pas symétrique, on la corrige
    if not symetrique:
        print("L'image n'est pas symétrique verticalement, correction en cours...")
        for i in range(n):
            for j in range(m // 2):
                tab[i][m-1-j] = tab[i][j]  # Copier la partie gauche vers la droite
    else:
        print("L'image est déjà symétrique verticalement.")

    return tab

# Fonction pour négativer une image
def Negatif(tab):
    n = len(tab)
    m = len(tab[0])
    # Créer une nouvelle image pour le négatif
    negatif = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            negatif[i][j] = 1 - tab[i][j]  # Inverser : 0 devient 1, 1 devient 0

    return negatif

# Fonction pour superposer deux images (OU logique)
def Superposition(tab1, tab2):
    n = len(tab1)
    m = len(tab1[0])
    # Créer une nouvelle image pour la superposition
    resultat = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            # OU logique : si l'un des deux pixels est 0 (noir), le résultat est 0
            if tab1[i][j] == 0 or tab2[i][j] == 0:
                resultat[i][j] = 0
            else:
                resultat[i][j] = 1

    return resultat

#tableau de la figure
image = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Test des fonctions
print("Image initiale :")
AfficheImage(image)

# Vérification et correction de la symétrie
image_corrigee = VerifSymetrieVerif(image)
print("Image après correction de la symétrie :")
AfficheImage(image_corrigee)

# image corrigé
image_negatif = Negatif(image_corrigee)
print("Négatif de l'image corrigée :")
AfficheImage(image_negatif)

# superposition
print("Superposition de l'image initiale et de son négatif :")
image_superposee = Superposition(image, image_negatif)
AfficheImage(image_superposee)