import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory exists
output_dir = '/home/ubuntu/banking_legacy_modernization/outputs'
os.makedirs(output_dir, exist_ok=True)

# Load golden master results
data_path = '/home/ubuntu/banking_legacy_modernization/golden_master_data.json'
with open(data_path, 'r') as f:
    golden_data = json.load(f)

# Flatten the JSON data for analysis
flattened_data = []
for entry in golden_data:
    flattened_data.append({
        'case_id': entry['test_case_id'],
        'risk_category': entry['input']['client_profile']['risk_category'],
        'is_vip': entry['input']['client_profile']['is_vip'],
        'loan_amount': entry['input']['loan_amount'],
        'term_months': entry['input']['loan_term_months'],
        'interest_amount': entry['expected_output']
    })

df = pd.DataFrame(flattened_data)

# Set style
sns.set_theme(style="whitegrid")

# 1. Distribution of Interest by Risk Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='risk_category', y='interest_amount', data=df, palette='viridis')
plt.title('Interest Amount Distribution by Risk Category', fontsize=15)
plt.xlabel('Risk Category', fontsize=12)
plt.ylabel('Interest Amount ($)', fontsize=12)
plt.savefig(f'{output_dir}/interest_by_risk.png')
plt.close()

# 2. Correlation between Loan Amount and Interest
plt.figure(figsize=(10, 6))
sns.scatterplot(x='loan_amount', y='interest_amount', hue='risk_category', data=df, alpha=0.6)
plt.title('Loan Amount vs Interest Amount', fontsize=15)
plt.xlabel('Loan Amount ($)', fontsize=12)
plt.ylabel('Interest Amount ($)', fontsize=12)
plt.savefig(f'{output_dir}/loan_vs_interest.png')
plt.close()

# 3. Average Interest Rate by Term
df['implied_rate'] = (df['interest_amount'] / df['loan_amount']) * 100
avg_rate = df.groupby('term_months')['implied_rate'].mean()

plt.figure(figsize=(10, 6))
avg_rate.plot(kind='bar', color='skyblue')
plt.title('Average Implied Interest Rate by Term (Months)', fontsize=15)
plt.xlabel('Term (Months)', fontsize=12)
plt.ylabel('Average Implied Rate (%)', fontsize=12)
plt.xticks(rotation=0)
plt.savefig(f'{output_dir}/rate_by_term.png')
plt.close()

print("Data analysis completed. Visualizations saved in banking_legacy_modernization/outputs/")
