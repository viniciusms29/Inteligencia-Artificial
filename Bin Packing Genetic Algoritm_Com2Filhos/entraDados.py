# -*- coding: utf-8 -*-
"""

@author: Vinícius
"""

from itens import *

class InputOutput():

	def __init__(self, NomeArquivo):

		self.NomeArquivo = NomeArquivo

		self.ListaItens = []

		ContaId = 1

		Arq = open(NomeArquivo, "r")

		for linha in Arq:

			Conteudo = linha.split()

			if Conteudo[0] == "#":

				continue

			elif Conteudo[0] == "K":
			
				self.Capacidade = int(Conteudo[1])

			elif Conteudo[0] == "N":
	
				self.NumItens = int(Conteudo[1])

			elif Conteudo[0] == "i":

				NovoItem = Item(ContaId, Conteudo[1], int(Conteudo[2]))
				self.ListaItens.append(NovoItem)
				ContaId += 1

		Arq.close()