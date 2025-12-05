import json
import os
import random

CAMINHO = "dados/coelhos.json"


def garantir_arquivo():
    if not os.path.exists("dados"):
        os.makedirs("dados")

    if not os.path.exists(CAMINHO):
        with open(CAMINHO, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)


def carregar_coelhos():
    garantir_arquivo()
    with open(CAMINHO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_coelhos(lista):
    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4)


# -------------------------
#  COELHOS ALEATÓRIOS
# -------------------------

def gerar_coelho_aleatorio():
    nomes = ["Pipoca", "Nuvem", "Sombra", "Florzinha", "Pompom", "Neblina", "Luna", "Bolinho"]
    classes = ["Guerreiro", "Tanque", "Mago"]

    nome = random.choice(nomes)
    classe = random.choice(classes)

    if classe == "Guerreiro":
        atk = random.randint(6, 10)
        defesa = random.randint(4, 7)
        hp = random.randint(30, 40)

    elif classe == "Tanque":
        atk = random.randint(3, 6)
        defesa = random.randint(8, 12)
        hp = random.randint(40, 55)

    else:  # Mago
        atk = random.randint(8, 12)
        defesa = random.randint(2, 5)
        hp = random.randint(22, 32)

    return {
        "nome": nome,
        "classe": classe,
        "atk": atk,
        "def": defesa,
        "hp": hp
    }


# -------------------------
#  CRIAÇÃO MANUAL
# -------------------------

def criar_coelho():
    garantir_arquivo()

    print("\n=== CRIAÇÃO DE COELHO ===")
    nome = input("Nome do coelho: ")

    print("Escolha a classe:")
    print("1 - Guerreiro")
    print("2 - Tanque")
    print("3 - Mago")

    classe = input("Classe: ")

    if classe == "1":
        classe = "Guerreiro"
        atk = random.randint(6, 10)
        defesa = random.randint(4, 7)
        hp = random.randint(30, 40)

    elif classe == "2":
        classe = "Tanque"
        atk = random.randint(3, 6)
        defesa = random.randint(8, 12)
        hp = random.randint(40, 55)

    elif classe == "3":
        classe = "Mago"
        atk = random.randint(8, 12)
        defesa = random.randint(2, 5)
        hp = random.randint(22, 32)

    else:
        print("Classe inválida.")
        return

    novo_coelho = {
        "nome": nome,
        "classe": classe,
        "atk": atk,
        "def": defesa,
        "hp": hp
    }

    coelhos = carregar_coelhos()
    coelhos.append(novo_coelho)
    salvar_coelhos(coelhos)

    print(f"Coelho {nome} ({classe}) criado com sucesso!")


def criar_coelho_aleatorio():
    garantir_arquivo()
    coelho = gerar_coelho_aleatorio()

    coelhos = carregar_coelhos()
    coelhos.append(coelho)
    salvar_coelhos(coelhos)

    print(f"\nCoelho aleatório criado:")
    print(f"Nome: {coelho['nome']}")
    print(f"Classe: {coelho['classe']}")
    print(f"ATK: {coelho['atk']}")
    print(f"DEF: {coelho['def']}")
    print(f"HP: {coelho['hp']}")
