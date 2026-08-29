# Entrada de dados
nome = input("Nome do astronauta: ").strip()
distancia = float(input("Distância da missão (km): "))
velocidade = float(input("Velocidade média (km/h): "))

#Validação de dados
if distancia <= 0 or velocidade <= 0:
    print("A distancia e a velocidade devem ser maiores que zero.")
else:
    # Cálculos
    tempo_horas = distancia / velocidade
    tempo_dias = tempo_horas / 24

    # Saída de dados
    print()
    print("=== Simulação de Missão Espacial ===")
    print(f"Astronauta {nome}, bem-vindo à simulação!")
    print(f"A viagem terá uma distância de {distancia:.0f} km.")
    print(f"Com velocidade média de {velocidade:.0f} km/h, o tempo estimado é:")
    print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
    print("Boa sorte na missão!")