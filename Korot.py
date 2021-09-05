import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_excel(r"C:\Users\ramie\Downloads\korot.xlsx",header=4,index_col='Ajanjakso')
mod=data.iloc[:-3]
red=mod.iloc[::-1]
red.columns=['Eonia','Euribor 1kk','Euribor 3kk','Euribor 6kk','Euribor 12kk']
r""" fig, ax = plt.subplots(figsize=(12,7))
ax.set_xlabel('Ajanjakso',fontsize=16)
ax.set_ylabel('Korko',fontsize=16)
ax.set_title('Korot 2008-2021',fontsize=16)
ax.plot(red)
plt.xticks(red.index[::12],rotation=30)
plt.gcf().subplots_adjust(bottom=0.15)
plt.show() """

def select_interest():
    interest=input('Which interest rate would you like to select?').lower()
    if interest=='eonia':
        print(red['Eonia'])
    elif interest=='Euribor': 
        ask=input('Specify the lenght of Euribor').lower()
        if ask=='1 kk' or ask=='1' or ask=='1kk':
            print(red['Euribor 1kk'])
        elif ask=='3kk' or ask=='3' or ask=='3 kk':
            print(red['Euribor 3kk'])
        elif ask=='6kk' or ask=='6' or ask=='6 kk': 
            print(red['Euribor 6kk'])
        elif ask=='12kk' or ask=='12' or ask=='12 kk':
            print(red['Euribor 12kk'])
        else:
            print(f'Euribor {ask} was not found')
    else:
        print(f'Please check spelling for {interest} or give a valid interest')
if __name__ == "__main__":
    select_interest()