from module import forca

idioma = input("[1] Português do Brasil\n[2] English\n")

print("Welcome to the Word Guessing Game!")

n_letters = int(input("With how many letter you want to play?  "))
dicio = 'dicios/dicio' + str(n_letters) + '.txt'
dificuldade = input("In what level do you want to play?\n[1] Easy\n[2] Medium\n[3] Hard\n[4] Super hard\n")

levels = {
    "1": n_letters * 6,
    "2": n_letters + 4,
    "3": n_letters + 2,
    "4": n_letters + 1
}

langs = {
    "1": "br",
    "2": "en"
}

functions = forca(n_letters, dicio, levels[dificuldade], langs[idioma])

functions.dicios()
palavra = functions.randword()
functions.tries(palavra)