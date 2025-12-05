import json
import os

def mostrar_stats():
    caminho = "dados/coelhos.json"

    if not os.path.exists(caminho):
        print("Nenhum coelho criado ainda.")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        coelhos = json.load(f)

    total = len(coelhos)

    print("==== ESTATÍSTICAS ====")
    print(f"Total de coelhos criados: {total}")
    print("=======================")

if __name__ == "__main__":
    mostrar_stats()
