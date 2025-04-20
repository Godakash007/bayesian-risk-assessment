from data_loader import load_data
from preprocess import preprocess_data
from threat_intel_loader import load_threat_intel
from risk_analysis import compute_total_risk
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# === Load and preprocess asset-vulnerability dataset ===
asset_filepath =  "C:/Users/AKASH A/bayesian-risk-assessment/data/asset_vulnerability_mapping_data.xlsx"
asset_df = load_data(asset_filepath)
df_clean = preprocess_data(asset_df)

# === Load threat intel data (used later or for report) ===
threat_intel_filepath =  "C:/Users/AKASH A/bayesian-risk-assessment/data/threat_intel_data.xlsx"
threat_intel_df = load_threat_intel(threat_intel_filepath)

# === Load threat actor-asset mapping ===

threat_actor_filepath =  "C:/Users/AKASH A/bayesian-risk-assessment/data/threat_actor_asset_mapping_data.xlsx"
threat_actor_df = pd.read_excel(threat_actor_filepath)
# Add attack types manually in code (TEMP PATCH)
attack_type_mapping = {
    "Insider": "Phishing",
    "External Hacker": "SQL Injection"
}
threat_actor_df["attack_type"] = threat_actor_df["threat_actor"].map(attack_type_mapping)


# === Load prior attack success rates ===
prior_path = "C:/Users/AKASH A/bayesian-risk-assessment/data/prior_attack_success_rate.xlsx"
prior_df = pd.read_excel(prior_path)

# === Compute final ranked risk scores with prior data ===
ranked_assets = compute_total_risk(df_clean, threat_actor_df, prior_df)

# === Save results ===
os.makedirs("output", exist_ok=True)
ranked_assets.to_excel("output/ranked_risk_assets.xlsx", index=False)

print("\n✅ Final risk scores (with prior success rates) saved to 'output/ranked_risk_assets.xlsx'")

# Top 10 risky assets
top10 = ranked_assets.head(10)

# Set style
plt.figure(figsize=(12, 6))
sns.barplot(x="asset", y="total_risk_score", data=top10, palette="Reds_r")
plt.title("Top 10 Riskiest Assets (Based on Bayesian Risk Score)", fontsize=14)
plt.xlabel("Asset")
plt.ylabel("Total Risk Score")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("output/top10_risk_assets.png")
plt.show()

# Define mitigation strategies based on asset type
mitigation_map = {
    "WebApp": "Use WAF, input validation, regular patching, pentesting.",
    "Database": "Encrypt data, restrict access, monitor logs, apply patches.",
    "Server": "Harden OS, enable MFA, patch regularly, use EDR.",
    "Workstation": "Apply security updates, use antivirus, enable firewall.",
    "IoTDevice": "Change default creds, segment network, disable unused ports."
}

# Function to extract asset type and fetch mitigation
def get_mitigation(asset):
    if "WebApp" in asset:
        return mitigation_map["WebApp"]
    elif "Database" in asset:
        return mitigation_map["Database"]
    elif "Server" in asset:
        return mitigation_map["Server"]
    elif "Workstation" in asset:
        return mitigation_map["Workstation"]
    elif "IoTDevice" in asset:
        return mitigation_map["IoTDevice"]
    else:
        return "General hardening, access control, monitoring."

# Add mitigation strategies to ranked assets
ranked_assets["Mitigation Strategy"] = ranked_assets["asset"].apply(get_mitigation)
print("\n🔐 Top 5 Risky Assets with Mitigation Strategies:\n")
for i, row in ranked_assets.head(5).iterrows():
    print(f"{row['asset']}: {row['Mitigation Strategy']}")
