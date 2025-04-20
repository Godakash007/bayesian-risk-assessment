import pandas as pd

def preprocess_data(df):
    # Step 1: Rename columns for consistency
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # Step 2: Handle missing values (if any)
    df = df.dropna(subset=["asset", "vulnerability", "cvss_score", "exploit_probability"])

    # Step 3: Normalize CVSS and probability if needed
    df["cvss_score"] = df["cvss_score"].astype(float)
    df["exploit_probability"] = df["exploit_probability"].astype(float)

    # Step 4: Optional - Add Risk Score (CVSS × Exploit Probability)
    df["risk_score"] = df["cvss_score"] * df["exploit_probability"]

    print("\n✅ Data preprocessing complete!")
    print(df.head())

    return df
