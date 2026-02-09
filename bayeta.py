import random

def frotar(n_frases: int = 1) -> list:
    frases = []

    with open("frases.txt", "r", encoding="utf-8") as f:
        todas = [line.strip() for line in f if line.strip()]

    for _ in range(n_frases):
        frases.append(random.choice(todas))

    return frases

