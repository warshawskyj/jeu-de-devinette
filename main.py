from random import randrange
QUIT = False


def demander_quitter():
    """demander jusqu'à l'utilisateur donne une reponse valide: True = quitter, False = rester"""
    while True:  # les returns vont sortir de la boucle
        reponse = input("Voulez-vous faire une autre partie (o/n)? ")  # demander
        if reponse == "n":
            print("Merci et au revoir...")
            return True
        elif reponse == "o":
            return False
        print("réponse invalide")


def demander_defaut():
    """demander si l'utilisateur veut utiliser les bornes par defaut: True si oui, sinon False"""
    while True:  # les returns vont sortir de la boucle
        reponse = input("Voulez-vous utiliser les bornes par défaut (o/n)? ")
        if reponse == "o":
            return True
        elif reponse == "n":
            return False
        else:
            print("réponse invalide")


def demander_borne(nom_borne):
    """demander la valeur de la borne ayant le nom nom_borne"""
    while True:  # le return va sortir de la boucle
        try:
            borne = int(input(f"Entrez la borne {nom_borne}: "))
            return borne
        except ValueError:  # pas un nombre entier
            print("Ceci n'est pas un nombre valide!")


# repeter jusqu'a la fin du jeu
while not QUIT:
    nb_essais = 0
    guessed = False  # variable qui determine si l'utilisateur a trouve le nombre
    # demander si l'utilisateur veut utiliser les bornes par defaut
    if demander_defaut():
        # initialiser les bornes avec les valeurs par odefaut
        MIN, MAX = 0, 1000
    else:  # demander les deux bornes
        MIN = demander_borne("minimale")
        MAX = demander_borne("maximale")
    # choisir le nombre
    nombre = randrange(MIN, MAX + 1)
    print(f"J’ai choisi un nombre au hasard entre {MIN} et {MAX}")
    print("À vous de le deviner...")
    while not guessed:  # repeter jusqu'à l'utilisateur devine le nombre
        try:
            essai = int(input("Entrez votre essai: "))
        except ValueError:  # pas un nombre entier
            print("Ceci n'est pas un nombre valide!")
        else:
            nb_essais += 1  # il faut seulement augmenter nb_essais si l'essai est valide
            if nombre < essai:
                print(f"Mauvais choix, le nombre est plus petit que {essai}")
            elif nombre > essai:
                print(f"Mauvaise réponse, le nombre est plus grand que {essai}")
            else:  # bonne reponse
                guessed = True
                print("Bravo! Bonne réponse")
                print(f"Vous avez réussi en : {nb_essais} essai(s).")
                QUIT = demander_quitter()  # voir si l'utilisateur veut joueur une autre partie
