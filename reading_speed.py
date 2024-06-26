# 7
# This program reads the reading timetables, calculates the average reading speed for each participant and then
# groups the results by target (and file). The results are saved to a CSV file and displayed in the console.

import pandas as pd
import os

# Directory containing the reading timetables (updated)
directory = 'reading_time_selected_target_tables'

# Initialize a list to store the reading speeds for each participant
all_reading_speeds = []

# Files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.csv')]

for file in files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(directory, file))

    # Check if the 'Selected target' column exists
    if 'Selected target' in df.columns:
        target = df['Selected target']
        df = df.drop(columns=['Selected target'])
    else:
        print(f"Warning: 'Selected target' column not found in {file}")
        continue

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Calculate the average reading speed for each participant
    reading_speeds = numeric_df.mean(axis=1, skipna=True)

    # Add the selected target and file name
    reading_speeds = pd.DataFrame({
        'participant': df.index,
        'reading_speed': reading_speeds,
        'selected_target': target,
        'file_name': file
    })

    all_reading_speeds.append(reading_speeds)

# Combine all data into one dataframe
combined_reading_speeds = pd.concat(all_reading_speeds)

# Calculate the average reading speed for each target and file
average_speeds_by_target = combined_reading_speeds.groupby(['file_name', 'selected_target'])['reading_speed'].mean()

# Make a directory to store the results
output_directory = 'reading_speeds'
os.makedirs(output_directory, exist_ok=True)

# Save the results to a CSV file
output_file = 'reading_speeds/average_reading_speeds_by_target.csv'
average_speeds_by_target.to_csv(output_file)

# Display the results without the file name and with spaces between groups
previous_file_name = None
for (file_name, target), speed in average_speeds_by_target.items():
    if file_name != previous_file_name:
        if previous_file_name is not None:
            print()  # Add a space
        previous_file_name = file_name
    print(f"{target}: {speed:.2f} ms/word")


# Save the displays results to a text file in the same directory as the CSV file
output_text_file = 'reading_speeds/average_reading_speeds_by_target.txt'
with open(output_text_file, 'w') as f:
    previous_file_name = None
    for (file_name, target), speed in average_speeds_by_target.items():
        if file_name != previous_file_name:
            if previous_file_name is not None:
                f.write('\n')  # Add a space
            previous_file_name = file_name
        f.write(f"{target}: {speed:.2f} ms/word\n")
