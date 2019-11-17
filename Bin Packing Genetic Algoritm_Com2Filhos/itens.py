# -*- coding: utf-8 -*-
"""

@author: Vinícius
"""

class Item():

	def __init__(self, Id, Nome, Volume):
		self.Id     = Id
		self.Nome   = Nome
		self.Volume = Volume

	def __str__(self):
		return "(" + str(self.Id) + ") " + self.Nome + ": " + str(self.Volume)