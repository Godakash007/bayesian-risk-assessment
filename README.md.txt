# Bayesian Risk Assessment Using Cybersecurity Data

This project implements a Bayesian Network-based risk assessment framework to evaluate and rank the likelihood of cybersecurity threats compromising various digital assets.

## 🔍 Objective
To identify high-risk assets by:
- Analyzing vulnerabilities, threat actors, and exploit probabilities
- Calculating posterior probabilities using Bayesian inference
- Prioritizing mitigation based on total risk scores

## 📂 Project Structure

📁 bayesian-risk-assessment/ ├── data/ │ ├── asset_vulnerability_mapping_data.xlsx │ ├── threat_actor_asset_mapping_data.xlsx │ ├── prior_attack_success_rate.xlsx │ ├── threat_intel_data.xlsx ├── output/ │ └── ranked_risk_assets.xlsx ├── src/ │ ├── data_loader.py │ ├── preprocess.py │ ├── risk_analysis.py │ ├── threat_intel_loader.py │ └── main.py ├── AkashA_BayesianRiskReport.pdf ├── requirements.txt └── README.md


## 🛠️ Tools & Libraries Used
- **pgmpy** – for Bayesian modeling
- **pandas** – for data manipulation
- **matplotlib** – for plotting
- **networkx** – for network graph layout

## 🚦 Risk Score Formula
```python
risk_score = cvss_score × exploit_probability
total_risk_score = risk_score × target_probability × success_rate

📊 Features
Data preprocessing & cleaning

Dynamic Bayesian inference

Asset risk ranking

Auto-generated mitigation strategies

📎 Final Report
👉 AkashA_BayesianRiskReport.pdf 

📫 Contact
Akash A
Email: akashcarmelite@gmail.com
