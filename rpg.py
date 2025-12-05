from stats import mostrar_stats
from batalha import lutar
from coelhos import criar_coelho, carregar_coelhos, criar_coelho_aleatorio

def menu_principal():
    while True:
        print("\n===== RPG DOS COELHOS =====")
        print("1 - Criar novo coelho")
        print("2 - Criar coelho aleatório")
        print("3 - Iniciar batalha")
        print("4 - Ver estatísticas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_coelho()

        elif opcao == "2":
            criar_coelho_aleatorio()

        elif opcao == "3":  
            coelhos = carregar_coelhos()
            if len(coelhos) < 2:
                print("Você precisa de pelo menos 2 coelhos para batalhar!")
            else:
                print("Selecione dois coelhos:")
                for i, c in enumerate(coelhos):
                    print(f"{i} - {c['nome']} ({c['classe']})")

                c1 = int(input("Coelho 1: "))
                c2 = int(input("Coelho 2: "))

                lutar(coelhos[c1], coelhos[c2])

        elif opcao == "4":
            mostrar_stats()

        elif opcao == "0":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()

    teste