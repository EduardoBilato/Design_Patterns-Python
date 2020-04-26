# -*- coding: UTF-8 -*-
from abc import ABCMeta,abstractmethod

class Estado_de_um_orcamento(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def aplica_desconto_extra(self,orcamento):
		pass

	@abstractmethod
	def aprova(self,orcamento):
		pass

	@abstractmethod
	def reprova(self,orcamento):
		pass

	@abstractmethod
	def finalizado(self,orcamento):
		pass


class Em_aprocavao(Estado_de_um_orcamento):
	def aplica_desconto_extra(self,orcamento):
		orcamento.desconto_extra += orcamento.valor * 0.02

	def aprova(self,orcamento):
		orcamento.estado_atual = Aprovado()

	def reprovado(self,orcamento):
		orcamento.estado_atual = Reprovado()

	def finalizado(self,orcamento):
		raise Exception('Orçamentos em aprovação não podem ir para finalizado')


class Aprovado(Estado_de_um_orcamento):
	def aplica_desconto_extra(self,orcamento):
		orcamento.desconto_extra += orcamento.valor * 0.05
	
	def aprova(self,orcamento):
		raise Exception('Orçamento já aprovado') 

	def reprova(self,orcamento):
		raise Exception('Orçamentos aprovados não podem ser reprovados')

	def finalizado(self,orcamento):
		orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):
	def aplica_desconto_extra(self,orcamento):
		raise Exception('Orçamentos reprovados nao recebem desconto extra')

	def aprova(self,orcamento):
		raise Exception('Orçamentos reprovados não podem sesr aprovados') 

	def reprova(self,orcamento):
		raise Exception('Orçamentos reprovados não podem ser reprovados novamento')

	def finalizado(self,orcamento):
		orcamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):
	def aplica_desconto_extra(self,orcamento):
		raise Exception('Orçamentos finaizados não recebem desconto extra')

	def aprova(self,orcamento):
		raise Exception('Orçamentos finaizados não podem ser aprovados novamente')

	def reprova(self,orcamento):
		raise Exception('Orçamentos finalizados não podem ser reprovados')

	def finalizado(self,orcamento):
		raise Exception('Orçamentos finaizados não podem ser finalizados novamente')


class Orcamento(object):
	
	def __init__(self):
		self._itens=[]
		self.estado_atual = Em_aprocavao()
		self.__desconto_extra = 0

	def aprova(self):
		self.estado_atual.aprova(orcamento)

	def reprova(self):
		self.estado_atual.reprova(orcamento)

	def finaliza(self):
		self.estado_atual.finalizado(orcamento)

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)
	def adiciona_desconto_extra(self,desconto):
		self.__desconto_extra += desconto


	@property
	def valor(self):
		total=0.0
		for item in self._itens:
			total+=item.valor
		return total - self.__desconto_extra

	def obter_itens(self):
		return tuple(self._itens)

	@property
	def total_itens(self):
		return len(self._itens)
	
	def adiciona_item(self,item):
		self._itens.append(item)

class Item(object):
	"""Classe de itens do orçamento"""
	def __init__(self, nome, valor):
		self._nome=nome
		self._valor=valor
			
	@property
	def valor(self):
		return self._valor
		
	@property
	def nome(self):
		return self._nome

if __name__ == '__main__':

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('ITEM - 1',100))
	orcamento.adiciona_item(Item('ITEM - 2',50))
	orcamento.adiciona_item(Item('ITEM - 3',400))

	print(orcamento.valor)
	orcamento.aprova()
	orcamento.finaliza()
	
