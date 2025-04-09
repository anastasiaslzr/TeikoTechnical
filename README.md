# TeikoTechnical
Teiko.Bio's Technical Exam 
Hi, this is Anastasia Salazar and here is the instructions decribing my code.

First, you'll notice there are two different .csv files, one called cell-count
and one called new_cell-count.csv.
The cell-count.csv is the original file provided to me. The new one is product of the code.

CellCount.py This file is to fulfill this requirement: 
Please write a Python program to convert cell count in cell-count.csv to relative frequency (in percentage) 
of total cell count for each sample. Total cell count of each sample is the sum of cells in the five populations 
of that sample. Please return an output file in CSV format with cell count and relative frequency of each 
population of each sample per line. 

The code starts off with declaring lists to hold the cell counts, to eventually total them. 
Then the opening of the cell-count.csv and storing of the different cell values. 
The lists are totaled up and then output into the new table format. With the relative frequency calculations.

To run the code make sure the cell-count.csv is in the same folder as the CellCount.py. Then run the CellCount.py file.
The new_cell-count.csv should be created where it will display the new information. 

treatment.py This file is to fulfill this requirement: Among patients who have treatment tr1, we are interested 
in comparing the differences in cell population relative frequencies of melanoma patients who respond (responders)
to tr1 versus those who do not (non-responders), with the overarching aim of predicting response to treatment tr1.
Response information can be found in column response, with value y for responding and value n for non-responding. 
Please only include PBMC (blood) samples.

The code starts out with creating empty sets to soon be filled with the sample and the condition. 
Then opening the cell-count.csv and storing the data. Then declared the target_condition (melanoma), and creates
a dictionary with two empty lists, to eventually sort and store the response data. 
Then, I open the new_cell_count.csv to grab the relative frequency data 

Now, I created the boxplots using matplotlib and seaborn. And do the statistical math for the p values. 
IF the p value is <= 0.05 the two relative frequencies (between responders and non responders) is significantly 
different. So, the p value is calculated and compared. Lastly, the data is displayed showing the significantly 
different results ONLY.

To run the code, make sure you already ran CellCount.py so that you have access to both cell-count.csv and 
new_cell-count.csv since both are necessary to run this file. Then run the treatment.py file.
After running it, the b-cell boxplot graph will appear, to see the next cell box plot click the EXIT button 
ON THE BOXPLOT, then the next cell will appear. Once you get to the last box plot (MONOCYTE) Then the code 
will ouput the statistical data in the terminal. 



I included the Database questions and prototype schema in a .txt file titled CellDatabase. 
I wasn't sure if it was needed in a particular database program, but since it didn't specify I assumed that 
it was not meant to be compiled and simply just a prototype. 
