
#chaine 1: chaine de reference
#chaine 2: chaine a comparer


#'' met les chiffre en str au lien de int par defaut
Chaine2='6931'

def saisie():
    #saisie du code utilisateur
    Chaine1 = input("renseignez le code PIN :")
    #verifier si le code contient 4 caractère
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

def caractèrenumerique(Chaine1):
    if(Chaine1. isnumeric()):
         comparer2chaine(Chaine1,Chaine2)
    else:
         print("des Chiffres SVP")
         saisie()

saisie()
