import pandas as pd

# 1. Create a "messy" list of customer data
data = {
    'Customer': ['TechCorp', 'DataSystems', 'CloudNine', 'TechCorp', 'BigData Co'],
    'Deal_Size': [50000, 25000, 120000, 50000, 75000],
    'Status': ['Closed', 'Pending', 'Closed', 'Closed', 'Pending']
}

# 2. Turn that list into a "DataFrame" (The fundamental AI/ML data structure)
df = pd.DataFrame(data)

# 3. Perform some "Account Manager" Analysis
# Let's find the total value of "Closed" deals
closed_deals_total = df[df['Status'] == 'Closed']['Deal_Size'].sum()

# 4. Clean the data (AI models hate duplicate data!)
clean_df = df.drop_duplicates()

print(f"--- Sales Report ---")
print(f"Total Revenue from Closed Deals: ${closed_deals_total}")
print(f"\nCleaned Customer List:\n{clean_df}")
