import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output directory exists
os.makedirs('/home/ubuntu/banking_legacy_modernization/outputs', exist_ok=True)

# Load golden master results
with open('/home/ubuntu/banking_legacy_modernization/golden_master_data.json', 'r') as f:
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

# 1. Distribution of Interest by Risk Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='risk_category', y='interest_amount', data=df, palette='Set2')
plt.title('Interest Amount Distribution by Risk Category')
plt.xlabel('Risk Category')
plt.ylabel('Interest Amount ($)')
plt.savefig('/home/ubuntu/banking_legacy_modernization/outputs/interest_by_risk.png')
plt.close()

# 2. Correlation between Loan Amount and Interest
plt.figure(figsize=(10, 6))
sns.scatterplot(x='loan_amount', y='interest_amount', hue='risk_category', data=df)
plt.title('Loan Amount vs Interest Amount')
plt.xlabel('Loan Amount ($)')
plt.ylabel('Interest Amount ($)')
plt.savefig('/home/ubuntu/banking_legacy_modernization/outputs/loan_vs_interest.png')
plt.close()

# 3. Average Interest Rate by Term
df['implied_rate'] = (df['interest_amount'] / df['loan_amount']) * 100
avg_rate = df.groupby('term_months')['implied_rate'].mean()

plt.figure(figsize=(10, 6))
avg_rate.plot(kind='bar', color='skyblue')
plt.title('Average Implied Interest Rate by Term (Months)')
plt.xlabel('Term (Months)')
plt.ylabel('Average Implied Rate (%)')
plt.xticks(rotation=0)
plt.savefig('/home/ubuntu/banking_legacy_modernization/outputs/rate_by_term.png')
plt.close()

print("Data analysis completed. Visualizations saved in /home/ubuntu/banking_legacy_modernization/outputs/")
