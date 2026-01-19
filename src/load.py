from pathlib import Path
import pandas as pd

def load(df: pd.DataFrame, output_path: str) -> None:
    path = Path(output_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(path, index=False, encoding='utf-8')
    return