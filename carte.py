import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv('C:/Users/SCHIPPKE/hackaton/pe-hackathon/significant-earthquake-database.csv', sep=';' , index_col='ID Earthquake')

print(df.head())



##df = pd.read_csv('significant-earthquake-database.csv', sep=';', index_col='ID Earthquake', usecols=['Flag Tsunami'])

