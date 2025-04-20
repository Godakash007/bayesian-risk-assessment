import pandas as pd

def load_threat_intel(filepath):
    if filepath.endswith(".xlsx") or filepath.endswith(".xls"):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format for threat intel")

    print("\n📥 Threat Intel Data Loaded!")
    print(f"🧾 Shape: {df.shape}")
    print("🕵️ Preview:")
    print(df.head())

    return df
