# 5
# This program creates a box plot for each sentence, showing the reading times of each word for each user.

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Input and output file paths
input_dir = 'reading_time_tables'
output_dir = 'box_plot_charts'
os.makedirs(output_dir, exist_ok=True)

# Iterate over each CSV file in the input directory
for file_name in os.listdir(input_dir):
    if not file_name.endswith('.csv'):
        continue
    file_path = os.path.join(input_dir, file_name)
    data = pd.read_csv(file_path)

    # Extract the sentence from the words in the first row
    words = data.columns[1:]
    sentence = ' '.join(words)

    # Convert the data to long format
    melted_data = data.melt(id_vars=['Participant ID'], var_name='Word', value_name='Reading Time')

    # Draw the box plot
    plt.figure(figsize=(15, 10))
    sns.boxplot(x='Word', y='Reading Time', data=melted_data, whis=1.5)

    plt.xticks(rotation=90)
    plt.title(f'Reading Times per Word in Sentence: {sentence}')
    plt.ylabel('Reading Time')
    plt.xlabel('Words')
    plt.tight_layout()

    # Save the chart
    output_path = os.path.join(output_dir, file_name[:-4] + '.png')
    plt.savefig(output_path)
    plt.close()
