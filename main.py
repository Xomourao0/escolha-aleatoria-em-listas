import random

personagens = ["astronauta", "dragão", "robô"]
lugares = ["em uma floresta amaldiçoada", "no espaço", "em Atlântida"] 
acoes = ["ele encontrou uma sereia", "fumou uma planta mágica", "fez amizade com um alienígena"]

chosen_personagem = random.choice(personagens)
chosen_lugares = random.choice(lugares)
chosen_acao = random.choice(acoes)

historia = (f"o {chosen_personagem} estava {chosen_lugares} e {chosen_acao}")

print (historia)
