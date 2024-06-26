# 3
# This program reads the CSV file 'cleaned_data.csv' and counts how many times each option was chosen by the users.


# Initialize an empty dictionary to store results
results = {}

# Target words to search for in column A
Lists = ['Lista 1', 'Lista 2', 'Lista 3', 'Lista 4', 'Lista 5', 'Lista 6', 'Lista 7', 'Lista 8', 'Lista 9', 'Lista 10']

# Path to your CSV file

# Open the CSV file and read its contents
with open('data/cleaned_data.csv', "r", encoding="utf-8") as csv_file:
    lines = csv_file.readlines()
    # Iterate over each row in the CSV file
    for row in lines:
        fields_frasi = row.strip().split(",")
        if len(row) >= 9:  # Ensure the row has at least two columns
            Selection = fields_frasi[9]  # Value in column A
            Word = fields_frasi[10]  # Value in column B
            due_opzioni = fields_frasi[13]
            # Check if value_a contains any of the target words
            if 'Selection' == Selection and Word not in Lists:
                if due_opzioni not in results:
                    results[due_opzioni] = {}
                if Word in results[due_opzioni]:
                    results[due_opzioni][Word] += 1
                if Word not in results[due_opzioni]:
                    results[due_opzioni][Word] = 1


# Print the results (dictionary)
print("Results:")
for key, value in results.items():
    print(f"{key}: {value}")
