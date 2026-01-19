from extract import extract
from transform import transform
from load import load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def run():
    df_raw = extract(BASE_DIR / "data/raw/bill.csv")
    df_transformed = transform(df_raw)
    load(df_transformed, BASE_DIR / "data/output/billProcessed.csv")
    
    print("Arquivo processado com sucesso")
    
if __name__ == "__main__":    
    run()