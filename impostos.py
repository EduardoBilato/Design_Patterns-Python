# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod # ABCde ABstraCt

class imposto(object):
	def __init__(self,outro_imposto = None):
		self.__outro_imposto = outro_imposto

	def calculo_do_outro_imposto(self,orcamento):
		if self.__outro_imposto is None:
			return 0
		return self.__outro_imposto.calcula(orcamento)

	@abstractmethod
	def calcula(self,orcamento):
		pass

class template_de_imposto_condicional(imposto):
	
	__metaclass__ = ABCMeta

	def calcula(self,orcamento):
		if self.deve_usar_maxima_taxacao(orcamento):
			return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
		else:
			return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

	@abstractmethod
	def deve_usar_maxima_taxacao(self,orcamento):
		pass

	@abstractmethod
	def maxima_taxacao(self,orcamento):
		pass

	@abstractmethod
	def minima_taxacao(self,orcamento):
		pass

#função de empacotacmento do decorator do python ----------------------------------
def IPVX(metodo_ou_funcao):
	def wrapper(self,orcamento): #recebe o self do ISS e o segundo parametro do ISS
		return metodo_ou_funcao(self,orcamento) + 50
	return wrapper
#----------------------------------------------------------------------------------


class ISS(imposto):
	#@IPVX #decorator do python
	def calcula(self,orcamento):
		return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

class ICMS(imposto):
	def calcula(self,orcamento):
		return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


class ICPP(template_de_imposto_condicional):
	
	def deve_usar_maxima_taxacao(self,orcamento):
		return orcamento.valor > 500

	def maxima_taxacao(self,orcamento):
		return orcamento.valor * 0.07
		
	def minima_taxacao(self,orcamento):
		return orcamento.valor * 0.05
		

class IKCV(template_de_imposto_condicional):
	
	def deve_usar_maxima_taxacao(self,orcamento):
		return orcamento.valor > 500 and _tem_item_maior_que_100_reais(orcamento)

	def maxima_taxacao(self,orcamento):
		return orcamento.valor * 0.1
		
	def minima_taxacao(self,orcamento):
		return orcamento.valor * 0.06
		
	def _tem_item_maior_que_100_reais(self,orcamento):
		for item in orcamento.obter_Itens():
			if item.valor > 100:
				return True
		return False

'''
strategy
factoring
duck-type
chain of responsability
template mathod
decorator
state
builder
observer
'''