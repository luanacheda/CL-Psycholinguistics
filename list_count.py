# 1
# This program reads the CSV file 'cleaned_data.csv' and counts how many times each list was chosen by the users.

import pandas as pd
import re


def count_list_choices(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Initialize a dictionary to store the counts of each list
    list_counts = {f"Lista {i}": 0 for i in range(1, 11)}

    # In column '# 11. Value.' find all rows that contain 'Lista'
    list_choices = data[data['# 11. Value.'].str.contains('Lista', na=False)]

    # Iterate over the rows and count the number of times each list appears
    for list_name in list_choices['# 11. Value.']:
        match = re.search(r"Lista (\d+)", list_name)
        if match:
            list_number = int(match.group(1))
            if 1 <= list_number <= 10:
                list_counts[f"Lista {list_number}"] += 1

    return list_counts


file_path = 'data/cleaned_data.csv'
list_counts = count_list_choices(file_path)

# Print each key-value pair on a new line
for list_name, count in list_counts.items():
    print(f"{list_name}: {count}")
