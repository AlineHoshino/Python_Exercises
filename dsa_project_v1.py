import random
from os import system, name


def clean_screen():

    # Windows
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def game():

    clean_screen()
    print("\nBem vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    words = [
        "abacate",
        "abacaxi",
        "acerola",
        "amora",
        "banana",
        "cacau",
        "caja",
        "caju",
        "caqui",
        "figo",
        "goiaba",
        "jaca",
        "laranja",
        "manga",
        "melancia",
    ]
    word = random.choice(words)

    letters_found = ["_" for letter in word]

    chances = 6

    wrong_letters = []

    while chances > 0:
        print(" ".join(letters_found))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(wrong_letters))

        attempt = input("\nDigite uma letra: ").lower()

        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    letters_found[index] = letter
                index += 1
        else:
            chances -= 1
            wrong_letters.append(attempt)

        if "_" not in letters_found:
            print("\nVocê venceu, a palavra era:", word)
            break

    if "_" in letters_found:
        print("\nVocê perdeu, a palavra era:", word)


if __name__ == "__main__":
    game()
    print("\nParabéns!Você está aprendendo programação em python com a DSA")
