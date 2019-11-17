# -*- coding: utf-8 -*-
"""
@author: Vinícius
"""
from itens        import Item
from pacotes   import *
from entradaDados2 import InputOutput
#from entraDados import InputOutput # expecificamente para os arquivos entrada01,02,03
from individuo	  import *
import            sys
import random

def ordenaPopulacao(populacao):
	populacao.sort(key = lambda x: x.Objetivo)

def selecionaPais(populacao):
	""" Selecao de pais por torneio. """
	ordenaPopulacao(populacao)
	
	pais = [populacao[0]]
	for i in range(1, len(populacao)):
		if(populacao[i].Pacotes == populacao[0].Pacotes):
			pais.append(populacao[i])

	if(len(pais) >= 2):
		shuffle(pais)
		return [pais[0], pais[1]]

	return [populacao[0], populacao[1]]

def crossover(pais):
	pai1 = pais[0]
	pai2 = pais[1]
	filho1 = []
	filho2 = []

	for i in range(0, len(pai1.VetItens)):
		# Filho 1:
		if(pai1.VetItens[i] not in filho1):
			filho1.append(pai1.VetItens[i]);
		if(pai2.VetItens[i] not in filho1):
			filho1.append(pai2.VetItens[i]);

		# Filho 2:
		if(pai2.VetItens[i] not in filho2):
			filho2.append(pai2.VetItens[i]);
		if(pai1.VetItens[i] not in filho2):
			filho2.append(pai1.VetItens[i]);

	return [filho1, filho2]


def mutacao(populacao, taxa):
	for filho in populacao:
		m = random.uniform(0, 1);
		if(m <= taxa):
			pos1 = random.randint(0, len(populacao[0]) - 1)
			pos2 = pos1
			while(pos1 == pos2):
				pos2 = random.randint(0, len(populacao[0]) - 1)

			aux = filho[pos1]
			filho[pos1] = filho[pos2]
			filho[pos2] = aux

def removerIndividuos(populacao):
	""" Remove os dois individuos menos aptos. """
	populacao.pop()
	populacao.pop()

def imprimePopulacao(populacao):
	print("Populacao:")
	for i in range(0, len(populacao)):
		print(populacao[i])

# Funcao principal da aplicacao
if __name__ == '__main__':

	if len(sys.argv) < 2 :

		print("\nERRO Sintaxe: python3 main.py <arq-entrada>\n")
		exit()

	entrada = InputOutput(sys.argv[1])

	# Parametros
	tamPopulacao = 40
	taxaMutacao = 0.3
	noGeracoes = 100

	# Cria a solucao inicial	
	populacao = []
	individuo = Individuo(entrada.ListaItens, entrada.Capacidade, None, 1)
	populacao.append(individuo)
	individuo = Individuo(entrada.ListaItens, entrada.Capacidade, None, 2)
	populacao.append(individuo)
	for i in range(2, tamPopulacao) :
		individuo = Individuo(entrada.ListaItens, entrada.Capacidade, None, 3)
		populacao.append(individuo)

	for i in range(0, noGeracoes):
		# Seleciona pais:
		pais = selecionaPais(populacao);

		# Cria offspring:
		filhos = crossover(pais);
		#print(filhos)

		# Mutacao:
		mutacao(filhos, taxaMutacao)
		#print(filhos)

		# Adiciona offspring:
		individuoF1 = Individuo(entrada.ListaItens, entrada.Capacidade, filhos[0], 3)
		individuoF2 = Individuo(entrada.ListaItens, entrada.Capacidade, filhos[1], 3)
		populacao.append(individuoF1)
		populacao.append(individuoF2)
		ordenaPopulacao(populacao)

		# Remove menos aptos:
		removerIndividuos(populacao)

		# Exibe melhor individuo:
		print("Geracao: " + str(i))
		print("Melhor individuo" + str(populacao[0]))

	arquivo = open('solucao.txt', 'w')
	arquivo.write("Solução do arquivo: " + sys.argv[1]+"\n")
	arquivo.write("Melhor individuo" + str(populacao[0]))
	arquivo.close()