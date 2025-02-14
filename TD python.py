continuer = True
import random #Import de la bibliotheque random
ips_attribuees = [] # liste pour stocker les ip
machines = {} # dictionnaire pour stocker les machines et leur ip

###################################################

def generer_ip():
    return f"192.168.1.{random.randint(1, 254)}" #genere une ip
continuer = True
IP = generer_ip()

#########################################################

def lister_ips2():
    if not machines:
        print("Aucune machine n'a d'IP attribuée.")
    else:
        print("machine et leurs IP:")
        for machine, ip in machines.items():
            print(f" - {machine}:{ip}")

#####################################################

def lister_ips():
    if not ips_attribuees:
        print("aucune IP attribuée")
    else:
        print("IP attribuees :")
        for ip in ips_attribuees:
            print(f" -{ip}")

        #####################################

while continuer:
    print("\n === Menu DHCP ===")
    print("1. Lister les IP attribuées")
    print("2. generer une IP aleatoire")
    print("3. Quitter")
    choix = input("\n Votre choix : ")

    if choix == "1":
        lister_ips2 ()
    elif choix =="2":
        nom_machine = input("Nom de la machine :")
        IP = generer_ip()
        machines[nom_machine] = IP
        print(f"IP  {IP} attribuée a {nom_machine}.")
    elif choix =="3":
        print("\n Au revoir !")
        continuer = False # sortir de la boucle
    else:
        print("\n chois invalide, veuillez réessayer.")
    