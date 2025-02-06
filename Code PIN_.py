
#chaine 1: chaine de reference
#chaine 2: chaine a comparer
#les 2 chaine doivent etre en str sinon code marche pas et si on met (0000 en int, on ressort avec 1 seul 0)
#chaine1 en str et chaine2 en int=code ne marche pas

#'' met les chiffre en str au lieu de int par defaut
Chaine2='6931'

def saisie():
    #saisie du code utilisateur
    Chaine1 = input("renseignez le code PIN :")
    #verifier la longueur de la saisie
    verifier4caractère(Chaine1)

# comparer 2 chaine de caractere
def comparer2chaine (chaine1,chaine2):
    if(chaine1==chaine2):
        print("CORRECT")
    else :
        print("INCORRECT")
        saisie()

# fonction pour vérifier la longueur 
def verifier4caractère(Chaine1):
    if(len(Chaine1)==4):
        caractèrenumerique(Chaine1)
    else:
        print("4 caractère SVP")
        saisie()
#verifier si c'est des caractere numerique et non lettres
def caractèrenumerique(Chaine1):
    if(Chaine1. isnumeric()):
         comparer2chaine(Chaine1,Chaine2)
    else:
         print("des Chiffres SVP")
         saisie()

saisie()
