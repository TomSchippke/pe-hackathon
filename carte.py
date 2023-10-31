import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv('C:/Users/SCHIPPKE/hackaton/pe-hackathon/significant-earthquake-database.csv', sep=';' , index_col='ID Earthquake')

print(df.head())


def magnitude(dataframe):

    ind_max=dataframe['EQ Primary'].idxmax()
    return ind_max


magnitude(df)


##fonction donnant les N tsunamis de plus grandes magnétude entre année 1 et année 2
##df = pd.read_csv('significant-earthquake-database.csv', sep=';', index_col='ID Earthquake', usecols=['Flag Tsunami'])
