# 4
# This program creates a table for each sentence and inserts the reading time of each word for each user.
# It then calculates the average, minimum, and maximum reading times for each word in each sentence.

import pandas as pd
import os


def analyze_reading_times(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Initialize a dictionary to store the reading times of each sentence
    sentence_data = {}

    # Convert the column '# 10. Parameter.' to numeric values where possible
    data['# 10. Parameter.'] = pd.to_numeric(data['# 10. Parameter.'], errors='coerce')

    # Iterate over the filtered rows
    for index in range(len(data)):
        row = data.iloc[index]
        if row['# 10. Parameter.'] == 1:
            sentence = row['# 16. Sentence (or sentence MD5).']
            participant_id = row['# 13. id.']
            words = sentence.split()

            if sentence not in sentence_data:
                sentence_data[sentence] = pd.DataFrame(columns=['Participant ID'] + words)

            # Iterate over the following lines to add the reading times for each word
            word_times = [None] * len(words)
            while index < len(data) and pd.notna(data.at[index, '# 10. Parameter.']):
                word_index = int(data.at[index, '# 10. Parameter.']) - 1
                reading_time = data.at[index, '# 14. Reading time.']

                if pd.notna(reading_time) and 0 <= word_index < len(words):
                    word_times[word_index] = reading_time

                index += 1

            # Add or update the reading time for the participant
            new_row = [participant_id] + word_times
            sentence_data[sentence] = pd.concat(
                [sentence_data[sentence], pd.DataFrame([new_row], columns=sentence_data[sentence].columns)],
                ignore_index=True)

    return sentence_data


def add_statistics(sentence_data):
    for sentence, df in sentence_data.items():
        # Calculate the statistics for each column (excluding 'Participant ID')
        numeric_df = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
        averages = numeric_df.mean().tolist()
        min_values = numeric_df.min().tolist()
        max_values = numeric_df.max().tolist()

        averages_row = ['Average'] + averages
        min_row = ['Min'] + min_values
        max_row = ['Max'] + max_values

        # Append the statistics rows to the DataFrame
        sentence_data[sentence] = pd.concat(
            [df, pd.DataFrame([averages_row], columns=df.columns), pd.DataFrame([min_row], columns=df.columns),
             pd.DataFrame([max_row], columns=df.columns)],
            ignore_index=True)

    return sentence_data


file_path = 'data/cleaned_data.csv'
sentence_data = analyze_reading_times(file_path)
sentence_data = add_statistics(sentence_data)


# Save each table in a separate CSV file
output_dir = 'reading_time_tables'
os.makedirs(output_dir, exist_ok=True)

for sentence, data in sentence_data.items():
    # Create a safe filename for the sentence
    file_name = ''.join(e for e in sentence if e.isalnum())[:50] + '.csv'
    output_path = os.path.join(output_dir, file_name)
    data.to_csv(output_path, index=False)
