# ETL Pipeline Python

**End-to-end ETL pipeline in Python with data cleaning, transformation, and CSV persistence.**

---

## Objetivo

Este projeto implementa uma **pipeline ETL (Extract, Transform, Load)** em Python para processar dados de vendas de gás e acessórios.  
O objetivo é demonstrar habilidades de **engenharia de dados**, incluindo:

- Leitura de arquivos CSV (`Extract`)
- Limpeza, padronização e validação de dados (`Transform`)
- Criação de métricas derivadas, como `total_Balance` e `product_Type`
- Persistência de dados tratados em arquivos CSV (`Load`)

O projeto serve como **exemplo de fluxo de dados completo**, pronto para ser expandido para bancos de dados ou relatórios analíticos.

---

## Tecnologias utilizadas

- Python 3.10+  
- Pandas  

---

## Estrutura do projeto

etl-pipeline-python/
│
├─ data/
│ ├─ raw/ ← arquivos CSV originais
│ │ └─ bill.csv
│ └─ output/ ← arquivos processados
├─ src/
│ ├─ extract.py ← função para ler CSV
│ ├─ transform.py ← função de limpeza e transformação
│ ├─ load.py ← função para salvar CSV final
│ └─ main.py ← script que orquestra o ETL
├─ README.md ← documentação do projeto
└─ .gitignore ← arquivos ignorados pelo Git


---

## Como executar

1. Clone o repositório:
git clone https://github.com/seu-usuario/etl-pipeline-python.git
cd etl-pipeline-python

2. Instale as dependências:
pip install pandas
   
3. Coloque seu CSV de dados brutos em:
data/raw/bill.csv

4. Execute o pipeline:
python src/main.py

5. Após a execução, o arquivo processado será gerado em:
data/output/billProcessed.csv

Exemplo de saída:
created_At,customer,product,category,quantity,unit_Price,total_Balance,product_Type
01/01/2024,Joao,GÁS P13,gas,2,120,240,GAS
02/01/2024,Ana,GÁS P13,gas,3,118,354,GAS
03/01/2024,Pedro,MANGUEIRA,acessorio,2,35,70,ACESSORIO




