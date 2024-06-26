# 6
# This program reads the cleaned data CSV file and the sentence tables, and updates the sentence tables with
# the selected target words.

import pandas as pd
import os


def sanitize_filename(sentence):
    return ''.join(e for e in sentence if e.isalnum())[:50]


def load_sentence_data(input_dir):
    sentence_data = {}
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv'):
            sentence_key = file_name[:-4]  # Remove the '.csv' extension
            sentence_data[sentence_key] = pd.read_csv(os.path.join(input_dir, file_name), dtype=str)
    return sentence_data


def process_selected_targets(file_path, sentence_data):
    # Read the CSV file
    data = pd.read_csv(file_path, dtype=str)

    # Iterate over the rows to find selections
    for index in range(1, len(data)):  # Start from the second row
        row = data.iloc[index]
        if row['# 10. Parameter.'] == 'Selection':
            target_word = row['# 11. Value.']
            prev_row = data.iloc[index - 1]
            sentence = prev_row['# 16. Sentence (or sentence MD5).']
            participant_id = row['# 13. id.']

            # Ensure the sentence is not NaN and prev_row contains a valid sentence
            if pd.notna(sentence):
                sanitized_sentence = sanitize_filename(sentence)
                # Check if the value is a word that needs to be added
                if target_word.startswith("Lista"):
                    continue
                else:
                    if sanitized_sentence in sentence_data:
                        sentence_df = sentence_data[sanitized_sentence]
                        # Ensure the column 'Selected target' exists
                        if 'Selected target' not in sentence_df.columns:
                            sentence_df['Selected target'] = None
                        sentence_df.loc[sentence_df['Participant ID'] == participant_id,
                                        'Selected target'] = target_word

    return sentence_data


# File path to the cleaned data CSV
file_path = 'data/cleaned_data.csv'

# Directory where the sentence tables are saved
input_dir = 'reading_time_tables'

# Load existing sentence tables
sentence_data = load_sentence_data(input_dir)

# Process selected targets and update the sentence tables
sentence_data = process_selected_targets(file_path, sentence_data)

# Save each updated table in a new directory
output_dir = 'reading_time_selected_target_tables'
os.makedirs(output_dir, exist_ok=True)

for sentence, data in sentence_data.items():
    # Create a safe filename for the sentence
    file_name = sanitize_filename(sentence) + '.csv'
    output_path = os.path.join(output_dir, file_name)
    data.to_csv(output_path, index=False)
