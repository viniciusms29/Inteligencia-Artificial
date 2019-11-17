"""

@author: Vinícius
"""

from itens import *

class InputOutput():

	def __init__(self, NomeArquivo):

		self.NomeArquivo = NomeArquivo

		self.ListaItens = []

		ContaId = -1

		Arq = open(NomeArquivo, "r")

		for linha in Arq:

			Conteudo = linha

			if ContaId == -1:	
				 self.NumItens = int(Conteudo)
				 ContaId = 0

			elif ContaId == 0:
				self.Capacidade = int(Conteudo)
				ContaId = 1

			elif ContaId != 0 or ContaId != -1:

				NovoItem = Item(ContaId, "item_"+ str(ContaId), int(Conteudo))
				self.ListaItens.append(NovoItem)
				ContaId += 1
				#print(NovoItem)

		Arq.close()