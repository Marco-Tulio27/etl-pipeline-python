import pandas as pd
from pathlib import Path
import sys
print(sys.executable)



def extract(csv_path : str) -> pd.DataFrame:    

    path = Path(csv_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Arquivo {csv_path} não encontrado")
    
    df = pd.read_csv(path, encoding='utf-8')

    return df    