#### IQB ASSIGNMENT 2

* **Team Members:-**
- Amandeep Kaur (2018014)
- Deepi Garg (2018389)
- Ria Gupta (2018405)

* **Python script:**​ iqb.py

* **Input:**​ 2 CSV format file (Default: test.csv, train.csv)

* **External support:** ​ GPS Raghava’s Pfeature (Pass train.csv(test.csv) to
Pfeature to get dipeptide_result_train.csv(dipeptide_result_test.csv))

* **Output:**​ 1 CSV format files (Default: output.csv)

* **Command to run the script:-**

Put train.csv, test.csv, dipeptide_result_train.csv, dipeptide_result_test.csv
in the same folder as the code file iqb.py and in terminal use the following
command.

`$ python3 iqb.py`

The python script uses the library sklearn to import svm.

- We define a function **dipeptite_composition(file)**, the function reads the file line-by-line and stores values of dipeptide compositions in a list of lists and returns it.

- We define **amino_composition(file, i)**, file is the input file on which
function works/reads and i is the number of the column to be read as the
column containing the amino acid sequence differs in the files, train.csv
and test.csv. The function reads the amino acids sequences one-by-one, and
for each sequence, creates a list which maintains the percentage frequency
count of each amino acid in the sequence.

`Percentage frequency count (A) = (Frequency count(A)/Length of sequence)*100`

The function returns a list of such lists for each sequence.

* **TRAINING**

The labels given in train.csv are copied into a list Y.
The methods amino_composition and dipeptide_composition are called on
train.csv and values are stored in lists X1 and X2 respectively.
For each sequence, the values in X1 are appended to X2.
Now a SVM is trained with values X2 and Y with 1 / (n_features * X.var()) as
the value of gamma. Once the SVM is trained, we proceed to test it.

* **TESTING**
The methods amino_composition and dipeptide_composition are called on
test.csv and values are stored in lists x1 and x2 respectively.
For each sequence, the values in x1 are appended to x2.
Now we call the pre-defined function predict() on the trained SVM(named
clf) and save results in the list ofile. These results are our output labels.
We create a new file, output.csv and for each ID of amino acid sequence in
test.csv we print the ID with its corresponding predicted label.