import random
import json
from datetime import datetime
import os

# -------------------------------
# Criar um coelhinho fofo
# -------------------------------
def criar_coelho():
    nomes = [
        "Cenourinha", "Pompom", "Sombra Fofa", 
        "Neve", "Bolinho", "Pipoca Saltitante",
        "Fofélio", "Marshmallow", "Bolinhas"
    ]

    return {
        "nome": random.choice(nomes),
        "vida": 10,
        "ataque": random.randint(1, 6)
    }

# -------------------------------
# Batalha entre dois coelhos
# -------------------------------
def rolar_dado():
    return random.randint(1, 6)

def lutar(c1, c2):
    print(f"\n🐰⚔️ {c1['nome']} VS {c2['nome']}\n")

    log = {
        "coelho1": c1["nome"],
        "coelho2": c2["nome"],
        "rounds": [],
        "vencedor": None,
        "timestamp": datetime.now().isoformat()
    }

    round_num = 1

    while c1["vida"] > 0 and c2["vida"] > 0:
        print(f"🎲 Round {round_num}")

        dano1 = rolar_dado() + c1["ataque"]
        dano2 = rolar_dado() + c2["ataque"]

        c2["vida"] -= dano1
        c1["vida"] -= dano2

        print(f"{c1['nome']} causou {dano1} de dano!")
        print(f"{c2['nome']} causou {dano2} de dano!\n")

        log["rounds"].append({
            "round": round_num,
            "dano1": dano1,
            "dano2": dano2,
            "vida1_restante": c1["vida"],
            "vida2_restante": c2["vida"]
        })

        round_num += 1

    vencedor = c1["nome"] if c1["vida"] > 0 else c2["nome"]
    log["vencedor"] = vencedor

    print(f"🎉 VENCEDOR: {vencedor}!\n")

    salvar_log(log)

    return vencedor

# -------------------------------
# Salvar log da batalha
# -------------------------------
def salvar_log(log):
    # garantir que a pasta existe
    os.makedirs("dados", exist_ok=True)

    with open("dados/batalha_log.json", "a", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False)
        f.write("\n")

# -------------------------------
# Executar o RPG
# -------------------------------
if __name__ == "__main__":
    coelhoA = criar_coelho()
    coelhoB = criar_coelho()

    lutar(coelhoA, coelhoB)

