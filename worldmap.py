# pour pouvoir exécuter le fichier, installer pygal : pip install pygal_maps_world
import pygal
import pandas as pd
import numpy as np

worldmap = pygal.maps.world.World()

codes = pd.read_csv("./codespays.csv", encoding="Latin1", sep=';',index_col='Country')
test = pd.read_csv("./dataframe_test.csv",sep=';')
#print(codes)

def dictionnaire(dataframe,colonne):
    df = codes.merge(dataframe, left_on = 'Country',right_on = 'Country')
    df.set_index('code', inplace=True)
    df[colonne].to_dict()


D = dictionnaire(test,'Magnitude')
worldmap.add('Magnitude',D)
worldmap.render()
worldmap


