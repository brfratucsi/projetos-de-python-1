import datetime


def tipo_de_unidade(unidade):
    if unidade == "dias":
        return print(f"Você tem  {tempo_restante.days + 1} dias para {tarefa}")
    elif unidade == "horas":
        tempo_restante_horas = int(tempo_restante.total_seconds() / 60 / 60)
        return print(f"Você tem  {tempo_restante_horas} horas para {tarefa}")


x = " "
while x != "exit":
    print("\nDigite a tarefa que você deve fazer e sua data prazo máximo, \no programa retornara seu tempo restante.")
    x = input("Exemplo de como passar a informação: Trocar cordas do violão-20.06.2021\n> ")

    dados = x.split("-")

    tarefa = dados[0]
    data_final = dados[1]

    data_atual = datetime.datetime.today()
    data_final = datetime.datetime.strptime(data_final, "%d.%m.%Y")
    tempo_restante = data_final - data_atual

    y = input("Em qual unidade você quer saber seu tempo restante? Digite 'dias' ou 'horas'.\n> ")
    tipo_de_unidade(y)





