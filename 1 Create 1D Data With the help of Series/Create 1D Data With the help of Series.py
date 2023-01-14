

import pandas as pd

data = {'Tushar':9.5 , 'Shreyas' : 8.5 , 'Akshay':7.5 , 'Junaid':6.5}
# type(data)

data = pd.Series(data)
data


print(data.ndim)


# b Find the highest GPA 

print(data.max())



# c find the lowest GPA

print(data.min())

# d find the average DPA stored by all students
print(data.mean())

print(avg = (data['Tushar'] + data['Shreyas'] + data['Akshay'] + data['Junaid'])/4
avg)
