import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv('C:/Users/SCHIPPKE/hackaton/pe-hackathon/significant-earthquake-database.csv', sep=';' , index_col='ID Earthquake')

#magnitude FINIE
def magnitude(dataframe,nombre,time, annee1,annee2):
    '''fonction renvoyant les 'nombre' premiers pays en terme de magnitude; si time=true, la fonction applique un filtre entre les années 1 et 2, sinon le dataframe renvoyé est "intemporel"'''

    datcut=dataframe[['Coordinates','Year','Country','EQ Primary']]
    datcut.sort_values(by='EQ Primary', axis=0, ascending = False, inplace=True)

    if time==True:
        masque_années=((datcut['Year']>=annee1) & (datcut['Year']<=annee2))
        return(datcut[masque_années].iloc[:nombre])
    return(datcut.iloc[:nombre])

magnitude(df,6,False,2010,2020)




##A-t-il-vonduit à un Tsunami?

earthquakes_tsunami = df[df['Flag Tsunami']=='Tsunami']
earthquakes_tsunami.replace('Tsunami',True)
earthquakes_tsunami = earthquakes_tsunami.drop(['Month','Day','Focal Depth','EQ Primary','Mw Magnitude','Ms Magnitude','Mb Magnitude','Ml Magnitude','MFA Magnitude','Unknown Magnitude','Intensity','State','Location name','Region code','Earthquake : Deaths','Earthquake : Deaths Description', 'Earthquake : Missing','Earthquake : Missing Description', 'Earthquake : Injuries', 'Earthquake : Injuries Description', 'Earthquake : Damage (in M$)' ,'Earthquake : Damage Description','Earthquakes : Houses destroyed','Earthquakes : Houses destroyed Description','Earthquakes : Houses damaged','Earthquakes : Houses damaged Description','Total Effects : Deaths','Total Effects : Deaths Description', 'Total Effects : Missing', 'Total Effects : Missing Description', 'Total Effects : Injuries', 'Total Effects : Injuries Description','Total Effects : Damages in million Dollars','Total Effects : Damage Description','Total Effects : Houses Destroyed','Total Effects : Houses Destroyed Description','Total Effects : Houses Damaged','Total Effects : Houses Damaged Description'], axis=1)

 

#reste à creer une dataframe avec (le nombre de tremblement de terres + tsunami) par pays

#et une autre avec le nombre de tremblement de terres  par pays

 

print(earthquakes_tsunami)