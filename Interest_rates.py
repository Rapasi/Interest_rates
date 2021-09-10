import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Selected paths work only on my computers

path_lnx='~/Rami/Python_projects/Interest_rates.xlsx'
path_windows=r'C:\Users\ramie\Downloads\korot.xlsx'

# Reading csv as pandas dataframe and modifying it a litle. 

data=pd.read_excel(path_lnx,header=4,index_col='Period')
mod=data.iloc[:-2]
red=mod.iloc[::-1]

# Changing column titles.

column_titles=['Eonia','Euribor 1kk','Euribor 3kk','Euribor 6kk','Euribor 12kk']
red.columns=column_titles

# Defining a function to graph plots.

def graph(Interest,Title):    
    fig=plt.figure(figsize=(12,7))
    plt.xlabel('Ajanjakso',fontsize=16)
    plt.ylabel('Korko',fontsize=16)
    plt.title(Title,fontsize=16)
    plt.plot(Interest)
    plt.xticks(red.index[::12],rotation=30)
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.legend()
    plt.pause(0.0001)

# The body

while True:
    interest=input('Which interest rate would you like to select? ').lower()
    if interest=='eonia':
        print(red['Eonia'])
        graph(red['Eonia'],f'{column_titles[0]} 1999-2021')
    elif interest=='Euribor' or interest=='euribor': 
        ask=input('Specify the length of Euribor. ').lower()
        if ask=='1 kk' or ask=='1' or ask=='1kk':
            print(red['Euribor 1kk'])
            graph(red['Euribor 1kk'],f'{column_titles[1]} 1999-2021')
        elif ask=='3kk' or ask=='3' or ask=='3 kk':
            print(red['Euribor 3kk'])
            graph(red['Euribor 3kk'],f'{column_titles[2]} 1999-2021')
        elif ask=='6kk' or ask=='6' or ask=='6 kk': 
            print(red['Euribor 6kk'])
            graph(red['Euribor 6kk'],f'{column_titles[3]} 1999-2021')
        elif ask=='12kk' or ask=='12' or ask=='12 kk':
            print(red['Euribor 12kk'])
            graph(red['Euribor 12kk'],f'{column_titles[4]} 1999-2021')
        else:
            print(f'Euribor {ask} was not found')
    elif interest=='All' or interest=='all':
            print(red)
            graph(red,f'All interest rates 1999-2021')
    else:
        print(f'Please check spelling for "{interest}" or give a valid interest.')
    rep=input('Would you like to graph another one? Y/N ').lower()
    if rep=='no' or rep=='n':
        break
    elif rep=='y' or rep=='yes':
        continue
    else:
        print('I asked you a simple question?!!')
        break
plt.show()

if __name__ == "__main__":
    pass