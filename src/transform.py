import pandas  as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    
    df["customer"] = df["customer"].str.title()
    df["product"] = df["product"].str.upper()
    df["category"] = df["category"].str.lower()
    
    df["created_At"] = pd.to_datetime(df["created_At"], dayfirst=True, errors='coerce')
    df["quantity"] = pd.to_numeric(df["quantity"], errors='coerce')
    df["unit_Price"] = pd.to_numeric(df["unit_Price"], errors='coerce')
        
    df = df[
        (df["quantity"] > 0) &
        (df["unit_Price"] > 0) &
        (df["created_At"].notna())
    ]    
    
    df["total_Balance"] = df["quantity"] * df["unit_Price"]
    df["product_Type"] = df["category"].apply(lambda x: "GAS" if x == "gas" else "acessorio")
    
    
    return df