import pandas as pd

def compute_total_risk(asset_df, threat_df, prior_df):
    # Step 1: Normalize all column names
    asset_df.columns = asset_df.columns.str.strip().str.lower()
    threat_df.columns = threat_df.columns.str.strip().str.lower()
    prior_df.columns = prior_df.columns.str.strip().str.lower()

    # Step 2: Merge asset-vulnerability + threat actor mapping
    merged = pd.merge(asset_df, threat_df, on="asset", how="inner")

    # Step 3: Merge with prior success rates on both threat_actor and attack_vector
    merged = pd.merge(
        merged,
        prior_df,
        left_on=["threat_actor", "attack_type"],
        right_on=["threat_actor", "attack_vector"],
        how="left"
    )

    # Step 4: Compute full risk score
    merged["total_risk_score"] = (
        merged["risk_score"] *
        merged["target_probability"] *
        merged["success_rate"]
    )

    # Step 5: Sort by risk
    ranked = merged.sort_values(by="total_risk_score", ascending=False)

    # Optional: Preview
    print("\n📊 Ranked Assets with Prior Success Rate Included:")
    print(ranked[["asset", "risk_score", "target_probability", "success_rate", "total_risk_score"]].head())

    return ranked
