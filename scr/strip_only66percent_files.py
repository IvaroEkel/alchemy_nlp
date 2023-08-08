import pandas as pd

# Define the file path
file_path = '../alchemy_texts/all_prediction_JJ.csv'

# Read the CSV file
data = pd.read_csv(file_path)


# Function to determine the specifier for labs/ops
def get_specifier_labs(row):
    lab_ops = float(row['% Lab/Ops'].strip('%'))
    if lab_ops >= 66:
        return 1
    return 0


# Function to determine the specifier for principles
def get_specifier_principles(row):
    principles = float(row['% Principles'].strip('%'))
    if principles >= 66:
        return 1
    return 0


# Apply the function to create the 'If Principles' column
data['If Principles'] = data.apply(get_specifier_principles, axis=1)

# Apply the function to create the 'If Labs/Ops' column
data['If Labs/Ops'] = data.apply(get_specifier_labs, axis=1)


# Print result to console
print(data)

# Save the filtered data to a new CSV file
output_path = 'filtered_training_set.csv'
data.to_csv(output_path, index=False)

print(f"Filtered data saved to {output_path}")
