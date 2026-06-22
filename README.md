# Carrito-Supremo

Carrito-Supremo is a learning project focused on price comparison, data quality and API development.

The goal is to build a backend system that helps users compare product prices across stores, simulate a shopping basket and understand price reliability.

## Current status

Week 1: Python basics, CSV data and simple product search.

## Problem

Many people need to make better shopping decisions with limited budgets. Product prices can change often, and it is difficult to compare stores manually.

## First MVP

The first version loads product prices from a CSV file, searches products by name and orders results by price.

## Current features

- Load product price data from a CSV file.
- Search products by name.
- Sort search results by price.
- Show store, price and data confidence level.
- Handle searches with no results.

## Tech stack

Current:

- Python
- CSV
- Git / GitHub

Planned:

- Pandas
- SQLite
- FastAPI
- Pytest
- Docker
- Safe AI explanation module

## Project rule

Python calculates.  
SQL stores.  
FastAPI exposes.  
Pytest checks.  
Docker packages.  
AI explains but does not invent critical data.

## Project structure

```text
carrito-supremo/
data/
  precios.csv
src/
  buscador.py
tests/
README.md
requirements.txt
.gitignore
```

## How to run

```bash
python src/buscador.py
```

## Example search

```text
¿Qué producto quieres buscar? arroz

arroz redondo 1kg | Lidl | 1.29 € | confianza: alta
arroz redondo 1kg | Mercadona | 1.35 € | confianza: alta
arroz redondo 1kg | DIA | 1.42 € | confianza: media
```

## Roadmap

1. CSV product search
2. Pandas data cleaning
3. Data quality rules
4. SQLite database
5. FastAPI endpoints
6. Pytest test suite
7. Docker setup
8. Safe AI explanation module