# IA Project 2 - Discount Recommendation POC

This project is a small proof of concept for an AI-assisted discount recommendation system for a supplement brand.

## Goal

Recommend whether a customer should receive no discount, a small discount, or a larger discount based on simple customer features and synthetic data.

## Suggested structure

- `data/` - synthetic datasets and generated CSV files
- `models/` - trained model artifacts
- `notebooks/` - exploration and experimentation
- `src/` - data generation, training, and utility code
- `app/` - web app for the demo
- `docs/` - presentation notes and supporting material



## Biblioteca mas adequeada a ser utilizada
scikit-learn (SKLearn) -> para o modelo 
Streamlit -> para a web app

## Modelo recomendado:


Decision Tree ou Random Forest



## Next steps

1. Generate synthetic customer data.
2. Train a simple classification model.
3. Build a small web app to show the recommendation.
4. Prepare the presentation slides.


## Produto final:
Uma web app para a empresa de suplementos, ou seja, uma ferramenta usada pela empresa


omo funcionaria na prática
Cenário

A empresa quer decidir:

“Devemos dar desconto a este cliente?”

Então a aplicação teria algo como:

Informação do Cliente
Compras por ano
Valor médio gasto
Última compra
Cliente novo?

Depois carregam em:

“Analisar Cliente”

E o sistema responde:

“Desconto recomendado: 10%”
“Probabilidade de retenção: alta”
“Cliente em risco de abandono”