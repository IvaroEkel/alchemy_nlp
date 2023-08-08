import pandas as pd

# Define the file path
file_path = '../alchemy_texts/all_prediction_JJ.csv'

# Read the CSV file
data = pd.read_csv(file_path)


# Function to determine the specifier for each row
def get_specifier(row):
    principles = float(row['% Principles'].strip('%'))
    lab_ops = float(row['% Lab/Ops'].strip('%'))
    if principles >= 66 and lab_ops >= 66:
        return "Both"
    elif principles >= 66:

        return "Principles"
    elif lab_ops >= 66:
        return "Lab/Ops"
    return None


# Apply the function to create the 'Specifier' column
data['Specifier'] = data.apply(get_specifier, axis=1)

# Filter the rows where the Specifier is not None
filtered_data = data[data['Specifier'].notna()]

# Print result to console
print(filtered_data)

# Save the filtered data to a new CSV file
output_path = 'filtered_training_set.csv'
filtered_data.to_csv(output_path, index=False)

print(f"Filtered data saved to {output_path}")
