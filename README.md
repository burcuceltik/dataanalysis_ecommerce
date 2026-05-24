# E-Commerce Data Analysis with PostgreSQL

This project uses the Olist e-commerce dataset to practice data analysis and database design.

The main idea is simple: explore the raw CSV files, design a PostgreSQL database, load the data, and answer business questions with SQL and Python.

## Dataset

Olist Brazilian E-Commerce Public Dataset  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset includes orders, customers, products, sellers, payments, deliveries, and customer reviews.

Raw CSV files should be placed in `data/raw/`. They are not uploaded to GitHub.

## Tools

- Python
- Pandas
- PostgreSQL
- SQL
- Jupyter Notebook
- Streamlit or Power BI
- Git and GitHub

## Project Structure

```text
verianalizi/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── sql/
├── src/
├── dashboard/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Plan

1. Download the dataset.
2. Explore the CSV files with Python.
3. Check data types, missing values, and duplicates.
4. Design the PostgreSQL tables.
5. Load the data into PostgreSQL.
6. Write SQL analysis queries.
7. Create charts with Python.
8. Build a simple dashboard.
9. Write the final findings.

## Analysis Questions

- Which states have the most orders?
- Which product categories bring the most revenue?
- Does late delivery affect review scores?
- How do orders change by month?
- Which sellers perform better?
- What is the average order value?

## Status

Project setup is ready. Next step: download the dataset and inspect the CSV files.
