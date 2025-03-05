# trouver les ingrédients dans la pizza
# trouver le numéro que possède les pizza 

nom = ["regina", "margherita", "romaine", "4 fromages", "calzone"]
ingredient = [["tomate", "mozzarella", "jambon", "champignons"],
            ["tomate", "mozzarella", "basilic", "huile d'olive"],
            ["tomate", "anchois", "origan", "huile d'olive"],
            ["mozzarella", "gorgonzola", "parmesan", "selles-sur-cher"],
            ["mozzarella", "jambon", "tomate", "oeufs"]
             ]

def pizza_avec_modif(tab):
    pizza_valide = 0
    numpizza = [99,99,99,99,99]
    print("quel ingrédient souhaitez vous dans votre pizza?")
    ingredient = (input("saisir ingrédient"))
    for I in range (5):
        for H in range (4):
            if tab[I][H] == ingredient:
                numpizza[pizza_valide] = I
                pizza_valide = pizza_valide +1
    return numpizza



liste_pizza = pizza_avec_modif(ingredient)
print (liste_pizza)
                


