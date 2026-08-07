# SmartPrice — Project Charter

## 1. Nome do projeto

**SmartPrice**

---

## 2. Visão

O SmartPrice pretende tornar mais simples e rápido encontrar bons preços para produtos na Internet.

O objetivo é reduzir o tempo que uma pessoa normalmente perde a pesquisar manualmente em várias lojas, comparando preços, procurando promoções e tentando perceber onde é mais vantajoso comprar.

O SmartPrice deverá pesquisar diferentes fontes, incluindo lojas portuguesas e internacionais, especialmente dentro do mercado europeu, e apresentar os resultados de forma simples e compreensível.

---

## 3. Problema

Encontrar o melhor preço para um produto pode ser uma tarefa demorada.

Um utilizador interessado num determinado produto pode ter de:

- pesquisar várias lojas;
- comparar preços manualmente;
- verificar diferentes países;
- confirmar se o produto é exatamente o mesmo;
- verificar disponibilidade;
- considerar custos de envio;
- acompanhar alterações de preço;
- procurar promoções.

Este processo pode consumir bastante tempo e ainda assim não garantir que o utilizador encontrou a melhor oportunidade disponível.

O SmartPrice pretende automatizar grande parte deste processo.

---

## 4. Objetivo principal

Criar uma plataforma capaz de:

1. identificar um produto;
2. pesquisar esse produto em várias fontes;
3. recolher os preços encontrados;
4. comparar os resultados;
5. identificar oportunidades relevantes;
6. apresentar a informação de forma clara ao utilizador.

---

## 5. Público-alvo

O SmartPrice destina-se principalmente a pessoas que:

- pesquisam regularmente preços antes de comprar;
- procuram promoções;
- comparam várias lojas;
- compram produtos de tecnologia;
- compram eletrodomésticos;
- compram produtos de áudio;
- compram produtos de outras categorias;
- estão dispostas a comprar em lojas europeias quando isso representar uma vantagem.

O produto deverá ser suficientemente simples para ser utilizado por qualquer pessoa, mesmo sem conhecimentos técnicos.

---

## 6. Tipos de produtos

O SmartPrice não será limitado a uma categoria específica.

A arquitetura deverá permitir trabalhar com diferentes tipos de produtos, incluindo inicialmente:

- Áudio
- Televisores
- Informática
- Telemóveis
- Eletrodomésticos
- Fotografia
- Gaming
- Casa
- Ferramentas
- Desporto
- Misc / Vários

A estrutura deverá permitir adicionar novas categorias no futuro sem alterações profundas na arquitetura.

---

## 7. Fontes de preços

O SmartPrice deverá ser construído para trabalhar com múltiplas fontes.

As fontes poderão incluir:

- lojas portuguesas;
- lojas espanholas;
- lojas francesas;
- lojas alemãs;
- lojas italianas;
- outras lojas europeias;
- marketplaces, quando apropriado.

A arquitetura deverá permitir adicionar novas fontes de forma modular.

O sistema não deverá depender de uma única loja.

---

## 8. Comparação internacional

Uma das características diferenciadoras do SmartPrice será a possibilidade de procurar preços fora de Portugal.

No entanto, o preço apresentado não deverá ser analisado isoladamente.

Sempre que possível, deverão ser considerados:

- preço do produto;
- moeda;
- custos de envio;
- disponibilidade;
- país de origem;
- entrega em Portugal;
- impostos ou outros custos relevantes.

O objetivo é encontrar o **melhor negócio realista para o utilizador**, e não simplesmente o número mais baixo encontrado na Internet.

---

## 9. Princípio de confiança

A confiança do utilizador é uma prioridade.

O SmartPrice deverá evitar apresentar como "melhor preço" um resultado que:

- corresponda a outro produto;
- seja de um produto usado quando o utilizador procura novo;
- seja apenas um acessório;
- esteja indisponível;
- tenha custos adicionais significativos;
- seja manifestamente incorreto.

Sempre que existirem limitações ou incertezas, o sistema deverá procurar comunicá-las claramente.

---

## 10. Arquitetura

O projeto deverá seguir uma arquitetura modular.

Os principais conceitos deverão ser separados:

```text
Produto
   ↓
Categoria
   ↓
Fontes / Lojas
   ↓
Resultados de preço