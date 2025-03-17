import random

class forca:
    def __init__(self, nivel, dir, dificuldade, idioma):
        self.nivel = nivel
        self.dir = dir
        self.dificuldade = dificuldade
        self.idioma = idioma

    def dicios(self):
        list = []

        dicionario = "dicios/" + self.idioma + ".txt"

        with open(dicionario, "r") as br:
            for line in br:
                word = line.strip()
                if len(word) == self.nivel:
                    list.append(word)

        newfile = "dicios/dicio" + str(self.nivel) + ".txt"
        counter = 0

        with open(newfile, "w") as new:
            for word in list:
                new.write(f"{list[counter]}\n")
                counter += 1
    
    def randword(self):
        listword = []

        with open(self.dir, "r") as dir:
            for line in dir:
                word = line.strip()
                listword.append(word)
            randnum = random.randint(0, len(listword))
        
        randword = listword[randnum]

        return randword

    def verify(self, tentativa, visual, palavra, erros):
        counter = 0
        visual_ = ""
        palavra = list(palavra)
        tentativa = tentativa.upper()
        for letter in palavra:
            letra = palavra[counter]
            if tentativa == letra:
                visual = list(visual)
                visual[counter] = tentativa
            counter += 1

        if tentativa in palavra:
            pass
        else:
            erros.append(tentativa)

        for i in range(len(visual)):
            visual_ += str(visual[i])

        return visual_, erros

    def tries(self, palavra):
        word = str(palavra).upper()
        visual = tentativa = ""
        erros = []

        for y in range(self.nivel):
            visual += "_"
        
        for i in range(self.dificuldade):
            counter = i
            if visual == word:
                break

            while True:
                tentativa = input(f"Try {counter + 1}: {visual} = ")
                if len(tentativa) == 1:
                    break
            
            visual, erros = self.verify(tentativa, visual, word, erros)
            print(f"You've taken wrong the following letters: {erros}")
            
        if visual == word:
            print(f"You got it!\nThe chosen word was {word}")
        else:
            print(f"You messed up ;-;\nThe chosen word was {word}")



