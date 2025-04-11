from random import randint

#parcourir  la collection
def collectioncomplete(collection):
    res = True
    for i in range(0, 9):
        if collection[i]==0:
            res = False
    return res

def ajoute(collection):
    nb_aleatoire = randint(0, 9)
    collection.append(nb_aleatoire)     #ajoute l'entier a la fin de la collection
    return collection

