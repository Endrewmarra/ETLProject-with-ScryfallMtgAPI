# MTG ETL Project — Scryfall API

Este projeto é um **pipeline ETL (Extract, Transform, Load)** desenvolvido em **Python**, que consome dados da **API pública da Scryfall** (Magic: The Gathering), processa grandes volumes de cartas em streaming e carrega os dados normalizados em um **banco NoSQL (MongoDB)**.

O objetivo é demonstrar conceitos reais de **engenharia de dados**, como:

- Consumo de API REST
- Download de dados em bulk
- Processamento de arquivos grandes (streaming)
- Normalização de dados
- Load idempotente em banco NoSQL
- Boas práticas com Git e ambientes virtuais

---

## Arquitetura do Projeto

extract → transform → load
(API)        (Python)        (MongoDB)

---

## Estrutura de pastas:

etl/
├─ extract.py
├─ transform.py
├─ load.py
└─ main.py
data/
└─ raw/ # Dados brutos (ignorado pelo Git)

---

## Tecnologias Utilizadas

- Python 3.10+
- Requests
- ijson (streaming JSON)
- MongoDB
- PyMongo

---

## Clonando o Repositório

```bash
git clone https://github.com/Endrewmarra/ETLProject-with-ScryfallMtgAPI.git
cd ETLProject-with-ScryfallMtgAPI
```

---

## Criando e Ativando o Ambiente Virtual

### Windows (PowerShell)

```bash
python -m venv venv
venv\Scripts\Activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalando as Dependências

```bash
pip install -r requirements.txt
```

Se ainda não existir um requirements.txt, ele deve conter pelo menos:

- requests
- ijson
- pymongo

---

## Pré-requisitos

- MongoDB instalado e em execução localmente
- Python
- VScode (ou outro editor de sua preferencia)

---

## Executando o Pipeline ETL

Com o ambiente virtual ativado:

```bash
python etl/main.py
```

O pipeline irá:

- Baixar os dados em bulk da Scryfall
- Processar o arquivo JSON em streaming
- Normalizar os dados das cartas
- Inserir os documentos no MongoDB

A carga é idempotente — rodar o pipeline mais de uma vez não cria duplicatas.

---

## Estrutura do Documento no MongoDB

Exemplo de carta armazenada:

```json
{
  "_id": "0000579f-7b35-4ed3-b44c-db2a538066fe",
  "name": "Fury Sliver",
  "set": "tsp",
  "set_name": "Time Spiral",
  "colors": ["R"],
  "type_line": "Creature — Sliver",
  "cmc": 6.0,
  "rarity": "uncommon",
  "main_type": "Creature"
}
```

---

## Observações Importantes

- Arquivos grandes de dados (data/raw/) não são versionados
- O projeto segue boas práticas de Git para projetos de dados
- Ideal para fins educacionais, portfólio e estudo de ETL

---

## Fonte dos Dados

API oficial da Scryfall: [https://scryfall.com/docs/api]([https://scryfall.com/docs/api]())
