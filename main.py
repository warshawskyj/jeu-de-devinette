from random import randrange


def demander_quitter():
    """demander jusqu'a l'utilisateur donne une reponse valide: True = quitter, False = rester"""
    while True:  # les returns vont sortir de la boucle
        reponse = input("Voulez-vous faire une autre partie (o/n)? ")  # demander
        if reponse == "n":
            print("Merci et au revoir...")
            return True
        elif reponse == "o":
            return False
        else:
            print("réponse invalide")


def demander_borne(nom_borne):
    """demander la valeur de la borne ayant le nom nom_borne"""
    while True:  # le return va sortir de la boucle
        try:
            borne = int(input(f"Entrez la borne {nom_borne}: "))
        except ValueError:  # pas un nombre entier
            print("Ceci n'est pas un nombre valide!")
        else:
            return borne


QUIT = False
while not QUIT:
    nb_essais = 0
    guessed = False
    #demander les deux bornes
    MIN = demander_borne("minimale")
    MAX = demander_borne("maximale")
    #choisir le nombre
    nombre = randrange(MIN, MAX + 1)
    print(f"J’ai choisi un nombre au hasard entre {MIN} et {MAX}.\nÀ vous de le deviner...")
    while not guessed:  # repeter jusqu'a l'utilisateur devine le nombre
        try:
            essai = int(input("Entrez votre essai: "))
        except ValueError: #pas un nombre entier
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
                QUIT = demander_quitter() #voir si l'utilisateur veut joueur une autre partie
