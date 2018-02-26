#Importa CVS
from dados import carregar_acessos
X, Y = carregar_acessos()

#90 Primeiras linhas para cada um deles
treino_dados = X[:90]
treino_marcacoes = Y[:90]

#10% dos que restaram para variável de teste, 9 ultimas linhas
teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

#Multinomial Naive Bayes é adequado para classificação com características discretas
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

#Preveja o Resultado
resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
 
print(taxa_de_acerto)
print(total_de_elementos) 
