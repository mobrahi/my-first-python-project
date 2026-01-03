import pandas as pd
import matplotlib.pyplot as plt

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

# 5. Group the data by Customer for the chart
summary = df_clean.groupby('Customer')['Deal_Size'].sum().sort_values(ascending=False)

# 6. Create the Bar Chart
plt.bar(summary.index, summary.values, color='skyblue', edgecolor='black')

# 7. Add Professional Labels (The "Account Manager" touch)
plt.title('Sales Pipeline: Total Deal Value by Customer', fontsize=14)
plt.xlabel('Customer Name', fontsize=12)
plt.ylabel('Deal Size ($)', fontsize=12)
plt.xticks(rotation=45) # Tilts names so they don't overlap
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 7. Save the chart as an image file
plt.tight_layout()
plt.savefig('sales_chart.png')
