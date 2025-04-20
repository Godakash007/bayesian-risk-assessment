import pandas as pd

def load_data(filepath):
 
    if filepath.endswith(".csv"):
        data = pd.read_csv(filepath)
    elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        data = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format.")
    
    print("✅ Data loaded successfully!")
    print(f"📊 Shape: {data.shape}")
    print("🧠 Preview:")
    print(data.head())
    
    return data

filepath = "C:/Users/AKASH A/bayesian-risk-assessment/data/asset_vulnerability_mapping_data.xlsx"
df = load_data(filepath)
