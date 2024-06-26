# 2
# This program reads the CSV file 'cleaned_data.csv' and counts how many times each sentence was read by the users.

import pandas as pd


def count_sentences(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Initialize a dictionary to store the counts of each sentence
    sentence_counts = {}

    # Convert the column '# 10. Parameter.' to numeric values where possible
    data['# 10. Parameter.'] = pd.to_numeric(data['# 10. Parameter.'], errors='coerce')

    # Filter rows where '# 10. Parameter.' is 1
    filtered_data = data[data['# 10. Parameter.'] == 1]

    # Iterate over the filtered rows
    for index, row in filtered_data.iterrows():
        sentence = row['# 16. Sentence (or sentence MD5).']  # Get the sentence
        if pd.notna(sentence):  # Ensure the sentence is not NaN
            if sentence in sentence_counts:
                sentence_counts[sentence] += 1
            else:
                sentence_counts[sentence] = 1

    return sentence_counts


file_path = 'data/cleaned_data.csv'
sentence_counts = count_sentences(file_path)

# Print each key-value pair on a new line
for sentence, count in sentence_counts.items():
    print(f"{sentence}: {count}")
