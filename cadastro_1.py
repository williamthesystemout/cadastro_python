from datetime import datetime
import random

name = input("Digite seu nome:\n")
idade = int(input("Digite sua idade:\n"))
aniversario = datetime.strptime(input("Digite sua data de aniversário:\n"), '%d/%m/%Y')
cartoes = ['R$ 25,00', 'R$ 50,00', 'R$ 100,00', 'R$ 120,00']
flag = datetime.now()
formatada = '%d/%m/%Y'
data_formatada = flag.strftime(formatada)
print("Olá", name, "seu registro foi concluído com sucesso no dia", data_formatada,".Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de", random.choice(cartoes))


