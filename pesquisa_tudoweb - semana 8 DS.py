def realizar_pesquisa(quantidade):
    excelentes = 0
    ruins = 0

    # Coleta os dados da quantidade definida de entrevistados.
    for numero in range(1, quantidade + 1):
        print(f"\n--- Entrevistado {numero} de {quantidade} ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opiniao = input("Como foi o atendimento? ")

        # Solicita novamente a opinião quando a opção é inválida.
        while opiniao not in ("1", "2", "3"):
            opiniao = input("Opção inválida. Digite 1, 2 ou 3: ")

        # Usa decisões para contar as opiniões solicitadas.
        if opiniao == "1":
            excelentes += 1
        elif opiniao == "3":
            ruins += 1

        print(f"Obrigado pela participação, {nome} ({idade} anos)!")

    print("\n=== RESULTADO DA PESQUISA TUDOWEB ===")
    print(f"Quantidade de entrevistados: {quantidade}")
    print(f"Respostas EXCELENTE: {excelentes}")
    print(f"Respostas RUIM: {ruins}")


if __name__ == "__main__":
    # testando com 50 entrevistados.
    realizar_pesquisa(50)