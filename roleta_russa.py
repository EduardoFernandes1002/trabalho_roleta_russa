import random

#Variaveis Globais
vida1 = 3
vida2 = 3
vez = 1
contador = 6

def escrever_txt(texto):
    with open("interface_roleta_russa.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def limpar_txt():
    with open("interface_roleta_russa.txt", "w", encoding="utf-8") as f:
        f.write("")

# Atualiza a interface do jogo
def atualizar_interface():
    texto = f"""
Jogador vez: {vez}
Vidas Jogador 1: {vida1}
Vidas Jogador 2: {vida2}
Tambores restantes: {contador}
""".strip()
    limpar_txt()
    escrever_txt(texto)

def trocar_vez(vez_atual):
    return 2 if vez_atual == 1 else 1

def perdeu_vida(vez, vidas):
    msg = f"Jogador {vez} perdeu uma vida: {vidas}"
    print(msg)
    escrever_txt(msg)

def atirar(escolhido, vidas):
    global contador, vez
    tem_bala = random.randint(1, contador)

    escolha_txt = f"Jogador {vez} escolheu {'atirar em si mesmo 😨' if escolhido == 1 else 'atirar no coleguinha 😏'}"
    print(escolha_txt)
    escrever_txt(escolha_txt)

    if tem_bala == 1:
        if contador >= 6:
            print("Hahaha azarão do caralho, levou de primeira")
            escrever_txt("Levou de primeira!")

        print("PPOOOWW~ 💥\nIh... deu ruim 😵")
        escrever_txt("Tiro! 💥")

        vez = trocar_vez(vez)

        contador = 7
        vidas -= 1

        if vez == 1 and escolhido == 2:
            perdeu_vida(2, vidas)
        elif vez == 2 and escolhido == 2:
            perdeu_vida(1, vidas)
        else:
            perdeu_vida(vez, vidas)
    else:
        print("Tick... Tick... Tick...\nUfa! Nenhuma bala! 😅")
        escrever_txt("Tick... sem bala 😅")

    atualizar_interface()
    return vidas

def escolha():
    global vida1, vida2, vez
    escolha = input("   1 - Atirar em si mesmo😨\n   2 - Atirar no coleguinha😊\n\nEscolha: ")

    match escolha:
        case "1":
            if vez == 1:
                vida1 = atirar(1, vida1)
            else:
                vida2 = atirar(1, vida2)
        case "2":
            if vez == 1:
                vida2 = atirar(2, vida2)
            else:
                vida1 = atirar(2, vida1)
            vez = trocar_vez(vez)
        case _:
            print("Escolha uma opção valida")
            escrever_txt("Escolha inválida")

# Limpa arquivo e escreve status inicial
limpar_txt()
atualizar_interface()

#Loop principal
while vida1 > 0 and vida2 > 0:
    print(f"\nJogador {vez} — suas vidas: {vida1 if vez == 1 else vida2}\nTambores restantes {contador}\n")
    escolha()
    contador -= 1
    atualizar_interface()

msg = ''
if vida1 == 0:
    msg = f"Jogador {vez} Ganhou com {vida2} vidas restantes"
elif vida2 == 0:
    msg = f"Jogador {vez} Ganhou com {vida1} vidas restantes"

print(msg)
escrever_txt(msg)
escrever_txt("Fim de jogo!")
print("Fim de jogo!")
