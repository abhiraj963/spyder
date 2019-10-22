'''
input any dataset and speicfy the model which is to be applied
answer the questions asked during the execution of the program
'''
import clean_data.determine_file as cd
import pandas as pd
path = input('enter the path to the training dataset: ')
i = 0
while path:
    

if cd.det_file(path) == 'csv':
    df = pd.read_csv(path)
elif cd.det_file(path) == 'xlsx':
    df = pd.read_excel(path)
    
cat_columns = input('enter the indices for categorical columns separated by spaces: ')
cat_columns = cat_columns.split()

print(df.head())
print(cat_columns)
