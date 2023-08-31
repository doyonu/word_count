# Ulysse Doyon
phrase = input("écrivez ce que vous voulez: ")

# compte le nombre de mot
def word_count():
    print("vous avez écrit",len(phrase.split(" ")),"mots")

word_count()