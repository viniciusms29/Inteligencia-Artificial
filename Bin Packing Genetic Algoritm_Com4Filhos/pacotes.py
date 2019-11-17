# -*- coding: utf-8 -*-
"""

@author: Vinícius
"""

class Pacotes():

	def __init__(self, Id, Capacidade):
		self.Id         = Id
		self.Capacidade = Capacidade
		self.LstItens   = []
		self.Ocupado    = 0
		
	@property
	def Livre(self):
		return self.Capacidade - self.Ocupado

	def InsereItem(self, Item):
		self.LstItens.append(Item)
		self.Ocupado = self.Ocupado + Item.Volume

	def RetiraItem(self, Item):
		self.LstItens.remove(Item)
		self.Ocupado = self.Ocupado - Item.Volume

	def __str__(self):
		StrSaida = "(" + str(self.Id) + "), Cap = " + str(self.Capacidade) + ", Ocp = " + str(self.Ocupado) + ", Livre = " + str(self.Livre) + "\n"

		for item in self.LstItens:
			StrSaida = StrSaida + "\t" + str(item) + "\n"

		return StrSaida