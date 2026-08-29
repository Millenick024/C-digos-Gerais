# Entrada de dados
nome = "Millena Monteiro Pinto da Silva"
distancia = 1000000.0
velocidade = 5000.0

# Cálculos
tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

# Saída de dados
print()
print(f'Astronauta {nome}, bem vindo(a) à simulação!')
print(f'A viagem terá uma distância de {distancia:.0f} km.')
print(f'Com velocidade média de {velocidade:.0f} km/h, o tempo estimado é de {tempo_dias:.0f} dias.')
print(f'{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).')
print('Boa sorte na missão!')


