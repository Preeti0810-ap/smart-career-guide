import pandas as pd

# Load your dataset (update the filename if needed)
df = pd.read_csv(r"D:\Projects\smart-career-guide\Student_Performance_data.csv")

# Display column names
print("Column names:\n", df.columns)

# Display first few rows
print("\nFirst 5 rows:\n", df.head())

