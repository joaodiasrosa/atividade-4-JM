from abc import ABC, abstractmethod
import random


class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao
    def validar_cartao(self):
        if len(self.numero_cartao) == 16 and self.numero_cartao.isdigit():
            print("Cartão válido.")
            return True
        else:
            print("Cartão inválido. Por favor, verifique o número")
            return False
    def processar_pagamento(self, valor):
        if self.validar_cartao():
            print(f"Pagamento de R${valor:.2f} processado com sucesso no cartão {self.numero_cartao}.")
        else:
            print("Pagamento não realizado devido a um cartão inválido.")


class PagamentoBoleto(Pagamento):
    def __init__(self):
        self.codigo_barras = ""
    def gerar_boleto(self):
        self.codigo_barras = "".join(str(random.randint(0, 9)) for _ in range(47))
        print(f"Código de barras gerado: {self.codigo_barras}")
    def processar_pagamento(self, valor):
        if self.codigo_barras:
            print(f"Pagamento de R${valor:.2f} processado com sucesso.")
        else:
            print("Pagamento não realizado. Gere um código de barras antes de processar o pagamento.")


print("---------- Pagamento com Cartão ----------")
pagamento_cartao = PagamentoCartao("1234567812345678") 
pagamento_cartao.processar_pagamento(250.75)
print("\n---------- Pagamento com Boleto ----------")
pagamento_boleto = PagamentoBoleto()
pagamento_boleto.gerar_boleto()
pagamento_boleto.processar_pagamento(450.60)



