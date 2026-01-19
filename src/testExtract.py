from extract import extract
from transform import transform
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df_raw = extract( BASE_DIR /  "data/raw/bill.csv")
df_transformed = transform(df_raw)

print(df_transformed.head())
