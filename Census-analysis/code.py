# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data,new_record),axis = 0)
#age distribution
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()
#race distribution
race_0 = []
race_1 = []
race_2 = []
race_3 = []
race_4 = []
for race in census[:,2]:
        if race == 0:
            race_0.append(race)
        elif race == 1:
            race_1.append(race)
        elif race == 2:
            race_2.append(race)
        elif race == 3:
            race_3.append(race)
        elif race == 4:
            race_4.append(race)
           

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
 
minority_race = min(len_0,len_1,len_2,len_3,len_4)


senior_citizens = census[census[:,0]>60]

working_hours_sum = np.sum(senior_citizens[0:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
avg_working_hours = round(avg_working_hours,2)
print(avg_working_hours)

#education vs job
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[0:,7])
avg_pay_low = np.mean(low[0:,7])

avg_pay_high ==avg_pay_low





