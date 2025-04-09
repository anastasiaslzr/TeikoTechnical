import csv
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
from collections import defaultdict

# Store condition and response by sample
condition_by_sample = {}
response_by_sample = {}

with open('cell-count.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        sample = row['sample']
        condition_by_sample[sample] = row['condition']
        response_by_sample[sample] = row['response']

# Target filter
target_condition = 'melanoma'

# Store data like: {cell_type: {'y': [...], 'n': [...]}}
cell_type_data = defaultdict(lambda: {'y': [], 'n': []})

with open('new_cell-count.csv') as nct_file:
    nct_reader = csv.DictReader(nct_file)
    for row in nct_reader:
        sample = row['sample']
        if condition_by_sample.get(sample) == target_condition:
            response = response_by_sample.get(sample)
            percent_str = row['percentage'].strip().replace('%', '')
            cell_type = row['population']
            try:
                percent_val = float(percent_str)
                if response in ['y', 'n']:
                    cell_type_data[cell_type][response].append(percent_val)
            except ValueError:
                continue  # skip bad data

# Generate a boxplot for each cell type
for cell_type, data in cell_type_data.items():
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=[data['y'], data['n']], palette='coolwarm')
    plt.title(f'{cell_type} Relative Frequency: Responders vs Non-Responders\n({target_condition})')
    plt.xticks([0, 1], ['Responders (y)', 'Non-Responders (n)'])
    plt.ylabel('Percent of Total')
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.tight_layout()
    plt.show()



# hich cell populations are significantly different in relative frequencies between responders and non-responders?
# Please include statistics to support your conclusion.
from scipy.stats import mannwhitneyu

for cell_type, data in cell_type_data.items():
    y_vals = data['y']
    n_vals = data['n']

    if len(y_vals) > 1 and len(n_vals) > 1:  # test needs more than 1 value
        stat, p_value = mannwhitneyu(y_vals, n_vals, alternative='two-sided')
        if p_value <= 0.05:
            print(f"{cell_type} is significantly different in relative frequencies.")
            print(f"{cell_type}: p = {p_value:.4f}")

