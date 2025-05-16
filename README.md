<p align="center">
  <img src="https://www.revio.com.br/wp-content/uploads/2024/06/Revio-logo.png" alt="Logotipo da Revio"/>
</p>

# 🖥️ Desafio Revio (Desenvolvedor Python)

Desafio de entrevista da Revio.
Considerar V2, V1 mantido por histórico.

## 👋 Introdução

Gostaria de agradecer pela oportunidade! Fazia um bom tempo que não utilizava Python e foi ótimo relembrar e reaprender. O desafio foi bem divertido, e como é algo que eu já trabalhava, ficou bem estruturado na minha cabeça.
A minha maior dificuldade foi a diferença de Javascript e Python, mesmo. Como fazia tempo que não usava, no começo assumi muita coisa mas depois que lembrei que Python é uma linguagem bem fácil de usar e potente, as coisas começaram a fluir muito mais rápido, o maior exemplo sendo achando que eu deveria marcar funções assíncronas como async e achar um jeito de realizar await, mas o Python já faz isso pra você, diferente de Javascript.

## 🎯 Desafio

- Adquirir lista de municípios de São Paulo
- Criar dictionary conténdo lista de cidades, com código (id) e nome da cidade
- Iterar pela lista e adquirir rank de nomes da cidade
- Criar dicionário conténdo município e frequência do nome GABRIEL para cada cidade que contém o nome GABRIEL no top 10
- Ordernar em ordem decrescente e salvar o dicionário em .json

## 💡 Explicação

Por estar meio enferrujado em Python, resolvi fazer o código aos poucos, buscando na documentação maneiras de fazer o que precisava. Fiz seguindo os passos que descrevi acima, nesta ordem.
Acabou ficando meio bagunçado mas funcional, e por isso, ficou como a primeira versão, neste repositório, denominada V1.
Depois fiz uma nova versão, aplicando melhor a POO, criando classes e métodos e utilizando-os. Assim, o código ficou mais organizado, e também um tanto mais DRY.

Uma explicação básica de como o código funciona é:
Criei uma classe IBGEAPI que lida com a própria API.
Acessamos essa classe para pegar a lista de todas as cidades de São Paulo com um simples fetch.
Depois, montamos o dicionário com as propriedades que chegaram.
Usando este mesmo dicionário, iteramos por ele, pegando cada cidade e alimentando na função da API que busca o ranking de nomes da cidade.
Se o nome está entre as 10 primeiras posições, salvamos a cidade e as informações do nome em 2 arrays diferentes
Depois de passar por todas as cidades, montamos o dicionário como o desafio pede, contendo a cidade e a frequência.
Com o dicionário de valores relevantes pronto, ordenamos em ordem decrescente baseado na frequência.
Pegamos o diretório atual e juntamos com "resultado.json" para termos o path final do arquivo resultante e salvamos.

## 👋 Fechamento

Queria novamente agradecer pela oportunidade que me proporam, foi um ótimo desafio e estou ansioso para ouvir mais de vocês!
