# Computational Psycholinguistics Project

This repository contains all the material we used for our project entitled "Sentences with long-distance agreement constructions: comparing reading speed and comprehension accuracy". The project is divided into two parts: the first part covers the experiment, and the second part involves the analysis programs.

## Experiment

In order to collect data, we designed an experiment using PCIbex. The code for this can be found in the `experiment_PCIbex.txt` file. The experiment itself can be accessed at this [link](https://farm.pcibex.net/p/VNnvnw/).

Participants had to input an ID of their choice. After a sentence to test self-paced reading, they were asked to randomly choose a list (1-10). Each list contained 25 sentences, which the users had to read at their own pace. After reading, participants completed the sentence with a target word. They had to choose between two target options, selecting the one they believed was most suitable.

After reaching 30 participants, we downloaded the data. The raw version can be found in the `data` directory (`downloaded_data.csv`). Cleaned versions of the data are also available in the same directory (both in Excel and CSV format). The `cleaned_data.csv` is the file we ran our programs on.

## Python Scripts and Order of Execution

Below are the programs we used to analyze the collected data. It is important to follow the order of execution. Results are reported in the `results.xlsx` file.

1. **`list_count.py`**  
   - **Description**: Reads the CSV file `cleaned_data.csv` and outputs the number of times that each list was chosen by participants.
   - **Usage**:  
     ```bash
     python list_count.py
     ```

2. **`sentences_count.py`**  
   - **Description**: Reads the CSV file `cleaned_data.csv` and outputs how many times each sentence was read by participants.
   - **Usage**:  
     ```bash
     python sentences_count.py
     ```

3. **`option_count.py`**  
   - **Description**: Reads the CSV file `cleaned_data.csv` and outputs how many times each option (target word) was chosen by the participants.
   - **Usage**:  
     ```bash
     python option_count.py
     ```

4. **`reading_time_tables.py`**  
   - **Description**: Creates a table for each sentence and inserts the reading time of each word for each user. It calculates the average, minimum, and maximum reading times for each word in each sentence. The generated tables can be found in the `reading_time_tables` directory.
   - **Usage**:  
     ```bash
     python reading_time_tables.py
     ```

5. **`box_plot_charts.py`**  
   - **Description**: Creates a box plot for each sentence, showing the reading times of each word for each user. The charts are saved in the `box_plot_charts` directory.
   - **Usage**:  
     ```bash
     python box_plot_charts.py
     ```
   - See also directory `box_plot_general`

6. **`selected_target.py`**  
   - **Description**: Reads the cleaned data CSV file and the sentence tables, updating the sentence tables with the selected target words. The updated tables are available in the `reading_time_selected_target_tables` directory.
   - **Usage**:  
     ```bash
     python selected_target.py
     ```

7. **`reading_speed.py`**  
   - **Description**: Reads the updated reading time tables, calculates the average reading speed for each participant, and then calculates the average reading speed for participants who chose the same target word, grouping the results by target and file. The results are saved in the `reading_speeds` directory both as a CSV and .txt file, and displayed in the terminal.
   - **Usage**:  
     ```bash
     python reading_speed.py
     ```

## How to Run

1. Clone this repository.
2. Ensure you have the necessary CSV files in the same directory as the scripts.
3. Run the scripts in the order specified above using Python.

