import random
from os import system, name


def clean_screen():

    # Windows
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')