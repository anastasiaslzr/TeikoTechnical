# here is my code 
import csv
from functools import total_ordering

# read data from the csv file
bcell = []
cd8cell = []
cd4cell = []
nkcell = []
mcell = []
sample = []

with open('cell-count.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # collect cell information into the corresponding list
        bcell.append(int(row['b_cell']))
        sample.append(row['sample'])
        cd8cell.append(int(row['cd8_t_cell']))
        cd4cell.append(int(row['cd4_t_cell']))
        nkcell.append(int(row['nk_cell']))
        mcell.append(int(row['monocyte']))

 # calculate the total cell count per each sample
total_b = sum(bcell)
total_cd8 = sum(cd8cell)
total_cd4 = sum(cd4cell)
total_nk = sum(nkcell)
total_m = sum(mcell)

# write new file -> new_cell-count.csv
with open('new_cell-count.csv', mode='w', newline='') as outfile:
    fieldnames = ['sample', 'total', 'population', 'count', 'percentage']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # read original csv file
    with open('cell-count.csv', mode='r') as infile:
        csv_reader = csv.DictReader(infile)

        for i, row in enumerate(csv_reader):
            # grab b-cell data and sample ids
            sample_id = row['sample']
            b_value = int(row['b_cell'])
            b_percent = (b_value/total_b) * 100
            writer.writerow({
                'sample': sample_id,
                'population': 'b_cell',
                'count': b_value,
                'total': total_b,
                'percentage': f"{b_percent:.2f}%"
            })

            # grab cd8_t_cell data
            cd8_value = int(row['cd8_t_cell'])
            cd8_percent = (cd8_value/total_cd8) * 100
            writer.writerow({
                'sample': sample_id,
                'population': 'cd8_t_cell',
                'count': cd8_value,
                'total': total_cd8,
                'percentage': f"{cd8_percent:.2f}%"
            })

            # grab cd4_t_cell data
            cd4_value = int(row['cd4_t_cell'])
            cd4_percent = (cd4_value/total_cd4) * 100
            writer.writerow({
                'sample': sample_id,
                'population': 'cd4_t_cell',
                'count': cd4_value,
                'total': total_cd4,
                'percentage': f"{cd4_percent:.2f}%"
            })

            # grab nk_cell data
            nk_value = int(row['nk_cell'])
            nk_percent = (nk_value/total_nk) * 100
            writer.writerow({
                'sample': sample_id,
                'population': 'nk_cell',
                'count': nk_value,
                'total': total_nk,
                'percentage': f"{nk_percent:.2f}%"
            })

            # grab monocyte data
            m_value = int(row['monocyte'])
            m_percent = (m_value/total_m) * 100
            writer.writerow({
                'sample': sample_id,
                'population': 'monocyte',
                'count': m_value,
                'total': total_m,
                'percentage': f"{m_percent:.2f}%"
            })


