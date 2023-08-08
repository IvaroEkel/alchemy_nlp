import pandas as pd


df = pd.read_csv('../alchemy_texts/all_prediction_JJ.csv', index_col=0)

def is_either_over_80(row):
    p = float(row['% Principles'].strip('%'))
    l = float(row['% Lab/Ops'].strip('%'))
    return p >= 80 or l >= 80

# Calculate the percentage for each column and check if both are over 80%
df['either_over_80'] = df.apply(is_either_over_80, axis=1)

# Convert the boolean values to 'True' and 'False'
df['either_over_80'] = df['either_over_80'].replace({True: 'True', False: 'False'})

# Save the result to a new CSV file
df.to_csv('all_prediction_updated_JJ.csv', index=False)