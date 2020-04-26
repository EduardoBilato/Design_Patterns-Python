# -*- coding: UTF-8 -*-

class Desconto_por_cinco_itens(object):
	def calcula(orcamento):
		return orcamento.valor * 0.1

class Desconto_por_mais_de_quinhentos_reais(object):
			def calcula(orcamento):
				return orcamento.valor * 0.07
						