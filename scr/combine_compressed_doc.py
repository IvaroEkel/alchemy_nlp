import pandas as pd

df1 = pd.read_csv('../alchemy_texts/texts_aka_compressed_documents.csv')
df2 = pd.read_csv('../alchemy_texts/texts_aka_compressed_documents2.csv')

starting_index = df1['Unnamed: 0'].iloc[-1] + 1

df2["Unnamed: 0"] = df2.apply(lambda row: int(row["Unnamed: 0"]) + starting_index, axis=1)

combined_df = pd.concat([df1, df2], ignore_index=True)

combined_df.to_csv("combined_compressed_doc.csv", index=False)
