#PERNA CURTA 1
#PERNA LONGA 0
#GORDO       1
#MAGRO       0
#FAZ ONC     1
#NÃO FAZ ONC 0

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]
 
dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

 #PORCO MARCADO COM 1
 #CACHORRO MARCADO COM -1
marcacoes = [1, 1, 1, -1, -1, -1]

#Essa biblioteca faz o treinamento baseado no algoritmo que se chama bayesiano.
from sklearn.naive_bayes import MultinomialNB

#O Multinomial é o algoritmo que usaremos para treinar o nosso modelo que diz se os nossos elementos são cachorros ou porcos.
modelo = MultinomialNB()

#Método para adequar o modelo
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [-1, 1, 1]

#Preveja o teste
resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print('RESULTADOS: ',resultado)
print('DIFERENÇAS: ',diferencas)
print('Total de Acertos:',total_de_acertos)
print('Total de Elementos:',total_de_elementos)
print('TAXA DE ACERTO: ',taxa_de_acerto)


