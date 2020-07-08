# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
#Checking all categorical values
categorical_var = bank_data.select_dtypes(include = 'object')
print(categorical_var)
#Checking all numerical values
numerical_var = bank_data.select_dtypes(include = 'number')
print(numerical_var)
#drop the column Loan_ID to create a new dataframe banks
banks = bank_data.drop('Loan_ID',axis=1)
#see the null values
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace = True)
banks.isnull()
print(banks.isnull().sum())

#Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'.
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
percentage_se = round((len(loan_approved_se)/614)*100,2)
print(percentage_se)
percentage_nse = round((len(loan_approved_nse)/614)*100,2)
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term = 0
for i in loan_term:
    if i>=25:
        big_loan_term+=1
print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)



