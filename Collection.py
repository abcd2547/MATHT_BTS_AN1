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

def collectionestcomplete(collection):
    for figurine in range(10):
        if collection.count(figurine) < 2:
            return False
        return True

def test():
    collection = []
    nb_achat = 0
    while not collectionestcomplete(collection):
        collection = ajoute(collection)
        nb_achats = nb_achats + 1
        print(f"Achat {nb_achat} : {collection}")
    return nb_achat, collection


