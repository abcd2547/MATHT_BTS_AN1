#fonction du calcul de moyenne
def calculmoy(note, coeff):
        somme_note = sum(note[1] * coeff[1] for i in range(7))
        somme_coeff = sum(coeff)
        moyenne = somme_note / somme_coeff
        return moyenne 
#decision de l'adminn en fonction de la note
def decision_admission(moyenne):
        if moyenne>=16:
                return "admis mention TB"
        elif moyenne >= 14:
                return "admis mention bien"
        elif moyenne >= 12:
                return "admis mention assez bien"
        elif moyenne >= 10:
                return "admis mention passable"
        else:
                return "refus"
#programme pour faire le calcul de moy       
def prog_principal():
        matiere = [
                "francais", "math", "H/G",
                "lv1", "lv2", "physique", "techno"
        ]
        coefficient = [3,3,2,2,1,2,1]
# saisir la note de la matiere
        notes = []
        for i in range (7):
                note = int(input(f"Saisissez la note pour{matieres[1]} : "))
                notes.append(note)


        moyenne = calculmoy(note, coeff)
#dis si admission ou non
        print(f"moyenne obtenu : {moyenne:.2f}")
        print(decision_admission(moyenne))