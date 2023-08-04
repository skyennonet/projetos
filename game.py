import random
import time

# Elementos
ELEMENTOS = {
    'Água': 0,
    'Fogo': 1,
    'Terra': 2
}

# Cartas
cartas = [
    {
        'nome': 'Espadachim',
        'atk': 4,
        'tecnica': 1,
        'equipamento': 0,
        'elemento': ELEMENTOS['Terra']
    },
    {
        'nome': 'Mago',
        'atk': 2,
        'tecnica': 5,
        'equipamento': 0,
        'elemento': ELEMENTOS['Água']
    },
    {
        'nome': 'Arqueiro',
        'atk': 3,
        'tecnica': 3,
        'equipamento': 1,
        'elemento': ELEMENTOS['Fogo']
    },
    {
        'nome': 'Cavaleiro',
        'atk': 5,
        'tecnica': 1,
        'equipamento': 2,
        'elemento': ELEMENTOS['Terra']
    },
    {
        'nome': 'Feiticeiro',
        'atk': 1,
        'tecnica': 6,
        'equipamento': 0,
        'elemento': ELEMENTOS['Água']
    },
    {
        'nome': 'Lanceiro',
        'atk': 3,
        'tecnica': 2,
        'equipamento': 1,
        'elemento': ELEMENTOS['Fogo']
    }
]

# Pontos de vida
hp_jogador1 = 20
hp_jogador2 = 20

# Função para escolher uma carta aleatória para o jogador 2 (IA)
def escolher_carta_ia():
    return random.choice(cartas)

# Função para calcular o dano e atualizar os pontos de vida
def calcular_dano(carta_atacante, carta_defensor, acao_ataque, acao_defesa):
    ataque_total = carta_atacante['atk'] + carta_atacante['tecnica'] + carta_atacante['equipamento'] + (2 if carta_atacante['elemento'] == carta_defensor['elemento'] else 0)
    defesa_total = carta_defensor['atk'] + carta_defensor['tecnica'] + carta_defensor['equipamento']
    
    if acao_ataque == 'atacar' and acao_defesa == 'atacar':
        dano = ataque_total // 2
    elif acao_ataque == 'atacar' and acao_defesa == 'defender':
        dano = max(0, ataque_total - 1)
    else:  # acao_ataque == 'defender' and acao_defesa == 'atacar'
        dano = max(0, ataque_total - 2)
    
    return dano

# Função para mostrar a situação atual do jogo
def mostrar_status():
    print("Jogador 1 - HP:", hp_jogador1, " | Carta:", carta_jogador1['nome'])
    print("Jogador 2 - HP:", hp_jogador2, " | Carta:", carta_jogador2['nome'])

# Jogador 1 (Controlado pelo jogador)
print("Escolha sua carta (Digite o número correspondente):")
for i, carta in enumerate(cartas, 1):
    print(f"{i}. {carta['nome']}")

escolha_jogador1 = int(input())

# Verificar se a escolha é válida
if 1 <= escolha_jogador1 <= len(cartas):
    carta_jogador1 = cartas[escolha_jogador1 - 1]
else:
    print("Escolha inválida. Escolhendo uma carta aleatória.")
    carta_jogador1 = random.choice(cartas)

# Jogador 2 (IA)
carta_jogador2 = escolher_carta_ia()

# Início da partida
tempo_inicial = time.time()  # Definindo o tempo inicial
tempo_limite = 180  # 3 minutos

print("Começou a batalha!")

# Loop principal do jogo (a partida durará até os pontos de vida de um dos jogadores chegarem a zero ou até o tempo limite ser atingido)
while hp_jogador1 > 0 and hp_jogador2 > 0:
    if time.time() - tempo_inicial >= tempo_limite:
        break  # O tempo limite foi atingido, encerra a partida

    # Turno do jogador 1
    print("Turno do jogador 1 (você):")
    print("Ações disponíveis: atacar, defender")
    acao_jogador1 = input("Digite sua ação: ").lower()

    # Verificar ação válida
    while acao_jogador1 not in ['atacar', 'defender']:
        print("Ação inválida. Tente novamente.")
        acao_jogador1 = input("Digite sua ação: ").lower()

    # Turno do jogador 2 (IA)
    acao_jogador2 = random.choice(['atacar', 'defender'])

    # Calcular dano
    dano_jogador1 = calcular_dano(carta_jogador1, carta_jogador2, acao_jogador1, acao_jogador2)
    dano_jogador2 = calcular_dano(carta_jogador2, carta_jogador1, acao_jogador2, acao_jogador1)

    # Atualizar pontos de vida
    hp_jogador1 -= dano_jogador1
    hp_jogador2 -= dano_jogador2

    # Mostrar resultado do turno
    print(f"Você causou {dano_jogador1} pontos de dano ao jogador 2.")
    print(f"O jogador 2 escolheu: {acao_jogador2}")
    print(f"O jogador 2 causou {dano_jogador2} pontos de dano a você.")
    mostrar_status()
    print()

# Verifica quem venceu
if hp_jogador1 <= 0 and hp_jogador2 <= 0:
    print("Empate!")
elif hp_jogador1 <= 0:
    print("Você perdeu!")
else:
    print("Você venceu!")
