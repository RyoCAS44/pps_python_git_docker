import random

def frotar(n_frases: int = 1) -> list:
    with open("frases.txt", "r", encoding="utf-8") as f:
        todas = [line.strip() for line in f if line.strip()]

    return [random.choice(todas) for _ in range(n_frases)]
