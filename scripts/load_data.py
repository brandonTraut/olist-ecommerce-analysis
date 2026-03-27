# Olist E-Commerce Data Ingestion Script
# Reads 9 CSVs from data/raw/ and loads them into Postgres as individual tables
# Prerequisites: PostgreSQL running, olist_db created, dependencies installed
# Update YOUR_PASSWORD before running

import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("postgresql://postgres:YOUR_PASSWORD@localhost:5432/olist_db")
csv_folder = "./data/raw/"

files = {
    "olist_customers_dataset.csv": "customers",
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_orders_dataset.csv": "orders",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "category_translation",
}

for filename, table_name in files.items():
    path = os.path.join(csv_folder, filename)
    df = pd.read_csv(path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f" {table_name} — {len(df):,} rows loaded")

print("\nAll tables loaded.")
