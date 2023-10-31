# pour pouvoir exécuter le fichier, installer pygal : pip install pygal_maps_world
import pygal
import pandas as pd
import numpy as np

worldmap = pygal.maps.world.World()

codes = pd.read_csv('C:/Users/clara/Cours-info/Hackathon/pe-hackathon/codespays.csv',index_col='Country')

def dictionnaire(dataframe,colonne):
    df = codes.merge(dataframe, left_on = 'Country',right_on = 'Country')
    df.set_index('code', inplace=True)
    df[colonne].to_dict()

def carte(dataframe,colonne):
    D = dictionnaire(dataframe,colonne)
    worldmap.add(D)
    worldmap.render()

