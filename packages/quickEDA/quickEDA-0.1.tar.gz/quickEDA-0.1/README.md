This is a very simple python package to do all EDA activities for any file.

How to use:
    
    pip install quickEDA

    import quickEDA 

    from quickEDA import eda

    eda("give your file path here")

Just pass the path of your file and get the exploratory data analysis done 
in few seconds.

1) Provides statistical information like count of values, Mean, Standard deviation, Minimun value, maximum value, 25%, 50% & 75% percentile of all the numerical columns
2) Provides overview of the file like number of columns present, data type of each column, null values present and memory space occupied by this dataset
3) Sample of first 5 rows
4) Sample of last 5rows
5) Correlation value between each column
6) No. of rows and columns present
7) Missing values in data & missing values percentage 
8) If duplicate rows present & dupliacte values percentage
9) Scatter matrix - to visualize the spread of data
10) Box plot to identify outliers
11) Column wise details
    1) Distinct values
    2) Missing values
    3) If zeroes present
    4) IQR
    5) lower outliers and percentage in each column
    6) upper outliers and percentage in each column
    7) Visualize distribution or each column
    8) Relationship between each x column with Y column

Things to Note:

    *Please place your 'Y' column or dependant feature as last column
    *If facing issue with path , try giving "c:\\Users\\...... (double slash)"