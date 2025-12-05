import random
import os

def registrar_log(texto):
    caminho = "dados/logs.txt"
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def lutar(c1, c2):
    print("\n==== BATALHA ====")
    print(f"{c1['nome']} VS {c2['nome']}\n")

    hp1 = c1["hp"]
    hp2 = c2["hp"]

    turno = 1

    while hp1 > 0 and hp2 > 0:
        print(f"-- Turno {turno} --")

        # Coelho 1 ataca
        dano1 = max(0, c1["atk"] - c2["def"] + random.randint(-2, 4))
        hp2 -= dano1
        print(f"{c1['nome']} causou {dano1} de dano. HP de {c2['nome']}: {hp2}")

        # Registrar no log
        registrar_log(f"{c1['nome']} causou {dano1} de dano em {c2['nome']}")

        if hp2 <= 0:
            break

        # Coelho 2 ataca
        dano2 = max(0, c2["atk"] - c1["def"] + random.randint(-2, 4))
        hp1 -= dano2
        print(f"{c2['nome']} causou {dano2} de dano. HP de {c1['nome']}: {hp1}")

        registrar_log(f"{c2['nome']} causou {dano2} de dano em {c1['nome']}")

        turno += 1
        print()

    # Final da batalha
    print("\n=== RESULTADO ===")

    if hp1 > 0:
        print(f"{c1['nome']} venceu!")
        registrar_log(f"VENCEDOR: {c1['nome']}")
    else:
        print(f"{c2['nome']} venceu!")
        registrar_log(f"VENCEDOR: {c2['nome']}")

    print("==================\n")
