import pandas as pd

# Define the file path
file_path = r"C:\Users\harip\Downloads\IBM Attrition Data\IBM Attrition Data\WA_Fn-UseC_-HR-Employee-Attrition (1).csv"

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())
print(df.shape)

print(df.isnull().sum())


duplicates = df.duplicated()

print(df[duplicates])

total_columns = df.shape[1]
print(f"Total number of columns: {total_columns}")


categorical_columns = df.select_dtypes(include=['object', 'category']).columns
print(f"Categorical columns: {len(categorical_columns)}")
print(f"Categorical columns list: {categorical_columns.tolist()}")

numerical_columns = df.select_dtypes(include=['number']).columns
print(f"Numerical columns: {len(numerical_columns)}")
print(f"Numerical columns list: {numerical_columns.tolist()}")


mappings = {
    'Education': {1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'},
    'EnvironmentSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'JobInvolvement': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'JobSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'PerformanceRating': {1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'},
    'RelationshipSatisfaction': {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'},
    'WorkLifeBalance': {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'}
}

df.replace(mappings, inplace=True)

unwanted_columns = ['Over18', 'EmployeeCount']
df.drop(columns=unwanted_columns, inplace=True)

# Save the processed data to a new CSV file
output_path = r"C:\Users\harip\Downloads\IBM Attrition Data\processed_data_replace.csv"
df.to_csv(output_path, index=False)

# Confirm the data has been saved
print(f"Processed data: {output_path}")
