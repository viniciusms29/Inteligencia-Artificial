# -*- coding: utf-8 -*-
"""

@author: Vinícius
"""

from pacotes import *
from itens  import Item
from math   import inf
from random import shuffle, random, randint
from copy   import deepcopy

class Individuo():

	def __init__(self, LstItens, Capacidade, Posicoes, ordena):

		self.VetItens        = []
		self.Objetivo        = 0
		self.ListaItens      = LstItens
		self.ListaPacotes = []
		self.Capacidade      = Capacidade
		self.Pacotes       = 0
		
		for i in range(1, len(LstItens)+1):
			self.VetItens.append(i)

		if(Posicoes == None):
			# Primeira geracao aleatoria:
			x = ordena
			if (x == 3):
				shuffle(self.VetItens)
			elif (x == 2):	#crescente
				self.VetItens.sort(key = lambda x: LstItens[x-1].Volume)
			elif (x == 1):	#decrescente
				self.VetItens.sort(key = lambda x: -LstItens[x-1].Volume)
		
		else:
			# Individuo com ordem predefinida:
			self.VetItens = Posicoes

		self.Decode();

		# Transforma uma solucao do espaco de codigo em espaco de solucoes
	def Decode(self):

		# Esvazia as listas de pacotes
		self.ListaPacotes = []

		# Cria o primeiro
		Contador      = 1
		NovoPacote = Pacotes(Contador, self.Capacidade)
		self.ListaPacotes.append(NovoPacote)
		self.Objetivo  = 1
		self.Pacotes = 1

		for idItem in self.VetItens:
			Inseriu = False
			for pacotes in self.ListaPacotes:
				if(self.ListaItens[idItem-1].Volume <= pacotes.Livre) :
					pacotes.InsereItem(self.ListaItens[idItem-1])
					Inseriu = True
					break

			if Inseriu == False:
				Contador = Contador + 1
				self.Pacotes += 1
				NovoPacote = Pacotes(Contador, self.Capacidade)
				self.ListaPacotes.append(NovoPacote)
				self.Objetivo = self.Objetivo + 1
				NovoPacote.InsereItem(self.ListaItens[idItem-1])


		for pacotes in self.ListaPacotes:

			Parcial = float(pacotes.Livre) / pacotes.Capacidade
			self.Objetivo += Parcial

	def avaliacao(self):
		return (self.Objetivo)
		#return len(self.ListaPacotes);

	def __str__(self):
		#return str(self.VetItens)
		
		StrOut = ""
		for pacotes in self.ListaPacotes:
			StrOut = StrOut + str(pacotes)

		StrOut = StrOut + "\nObjetivo = " + str(self.Objetivo) + ", Pacotes = " + str(self.Pacotes)

		return StrOut