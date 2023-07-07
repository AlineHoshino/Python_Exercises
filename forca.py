import random
print('Jogo da forca!')
print('Adivinhe a palavra abaixo:')
myList = ["banana", "uva", "pera", "abacate"]
aleatory_word = (random.choice(myList))
list_palavra = []
for letter in aleatory_word:
    list_palavra.append(letter)


def start_game():
    word_hide = {}
    for i in range(len(aleatory_word)):
        word_hide[i] = "_"
    print(word_hide.values())
    lifes = 6
    print(f"lifes - {lifes}")
    while lifes >= 0:
        if lifes == 0:
            return print("Fim do jogo")
        letter_choose = input("digite uma letra ")
        acerto = 0
        for i in range(len(aleatory_word)):
            if aleatory_word[i] == letter_choose:
                word_hide[i] = aleatory_word[i]
                acerto += 1
            print(word_hide[i])
        if acerto == 0:
            lifes -= 1
            print(f"lifes - {lifes}")
        if '_' not in word_hide.values():
            return print("ganhou")


start_game()
