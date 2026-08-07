# SmartPrice — Backlog

Este documento reúne funcionalidades, ideias e melhorias para o SmartPrice.

O backlog serve para registar ideias sem interromper o desenvolvimento da versão atualmente em construção.

Uma ideia adicionada ao backlog não significa que será imediatamente implementada.

---

## 🎯 Visão do produto

O SmartPrice pretende ajudar utilizadores a encontrar melhores preços para produtos em diferentes lojas e mercados, reduzindo o tempo necessário para pesquisar manualmente por promoções e oportunidades de compra.

O sistema deverá ser capaz de pesquisar produtos de diferentes categorias e comparar preços encontrados em várias fontes, incluindo lojas portuguesas e internacionais, especialmente dentro da Europa.

---

# 🚀 Prioridade atual — Produto base

Estas funcionalidades fazem parte do núcleo inicial que queremos construir.

## 1. Modelo de produtos

Criar uma estrutura de dados capaz de representar diferentes tipos de produtos.

Um produto deverá poder incluir, entre outros:

- Nome
- Marca
- Modelo
- Categoria
- Identificador do produto, quando disponível
- Características relevantes
- Imagem, futuramente

O sistema não deverá estar limitado a produtos de áudio.

---

## 2. Categorias de produtos

Criar um sistema de categorias para organizar os produtos.

Categorias iniciais previstas:

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
- Outros / Misc

A lista poderá crescer no futuro.

Também deverá existir uma categoria genérica:

**Misc / Vários**

para produtos que não se enquadrem nas categorias existentes.

---

## 3. Pesquisa por produto

O utilizador deverá conseguir indicar um produto que pretende encontrar.

Exemplos:

- LG OLED C5 65"
- Audio-Technica AT-LP70XBT
- Samsung Galaxy S26
- Bosch frigorífico
- Dyson aspirador

O sistema deverá procurar correspondências em diferentes fontes.

---

## 4. Comparação de preços

Para um determinado produto, o SmartPrice deverá conseguir apresentar os preços encontrados em diferentes lojas.

Exemplo:

| Loja | País | Preço | Link |
|---|---|---:|---|
| Loja A | Portugal | €1.399 | Ver produto |
| Loja B | Espanha | €1.299 | Ver produto |
| Loja C | Alemanha | €1.279 | Ver produto |

O sistema deverá conseguir identificar o melhor preço encontrado.

---

## 5. Suporte para múltiplas lojas

A arquitetura não deverá ficar dependente de uma única loja.

Deverá ser possível adicionar novas fontes sem alterar o funcionamento principal do sistema.

Exemplos de fontes que poderão ser suportadas futuramente:

- Amazon
- Worten
- Fnac
- MediaMarkt
- PcComponentes
- outras lojas europeias

A lista de lojas será definida e validada durante o desenvolvimento.

---

## 6. Pesquisa internacional

O SmartPrice deverá procurar oportunidades não apenas em lojas portuguesas.

A pesquisa deverá poder incluir mercados internacionais, especialmente:

- Espanha
- França
- Alemanha
- Itália
- Países Baixos
- outros mercados europeus relevantes

O objetivo é encontrar preços potencialmente mais competitivos do que os disponíveis em Portugal.

---

## 7. Informação geográfica e logística

Ao comparar preços internacionais, o sistema deverá futuramente considerar fatores como:

- País da loja
- Disponibilidade de entrega em Portugal
- Custos de envio
- Moeda
- IVA / impostos aplicáveis
- Possíveis custos adicionais
- Disponibilidade do produto

O preço apresentado como "melhor preço" deverá, idealmente, representar o custo real ou uma estimativa razoável do custo para o utilizador.

---

# 🔔 Funcionalidades futuras

Estas funcionalidades fazem parte da visão do produto, mas não devem interromper a construção da primeira versão.

## 8. Alertas de preço

Permitir ao utilizador definir um preço-alvo.

Exemplo:

> Quero comprar esta televisão se ficar abaixo de €1.200.

Quando o preço atingir o valor definido, o sistema deverá poder avisar o utilizador.

---

## 9. Histórico de preços

Guardar preços encontrados ao longo do tempo.

Permitir visualizar:

- Preço atual
- Preço anterior
- Preço mínimo encontrado
- Evolução do preço
- Data da última atualização

Futuramente poderá ser apresentado um gráfico de evolução.

---

## 10. Deteção de promoções

Identificar potenciais oportunidades de compra.

Exemplos:

- preço significativamente abaixo da média
- queda recente de preço
- novo preço mínimo
- promoção temporária

O sistema deverá evitar classificar automaticamente qualquer preço baixo como uma boa oportunidade sem contexto suficiente.

---

## 11. Normalização de produtos

Diferentes lojas podem apresentar o mesmo produto com nomes diferentes.

Exemplo:

```text
LG OLED C5 65"
LG OLED65C5
LG 65" OLED C5
LG OLED C5 65 inch