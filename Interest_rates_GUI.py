import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

Height=800
Width=1000

# Selected paths work only on my computers

path_lnx='~/Rami/Interest_rates/Interest_rates.xlsx'
path_windows=r'C:\Users\ramie\Downloads\korot.xlsx'

# Reading csv as pandas dataframe and modifying it a litle. 

data=pd.read_excel(path_lnx,header=4,index_col='Period')
mod=data.iloc[:-2]
red=mod.iloc[::-1]

# Changing column titles.

column_titles=['Eonia','Euribor 1kk','Euribor 3kk','Euribor 6kk','Euribor 12kk']
red.columns=column_titles

# Defining a function to graph plots.

def format(entry):
        if entry=='eonia':
            new='Eonia'
        elif entry=='Euribor' or entry=='euribor': 
            ask=input('Specify the length of Euribor ').lower()
            if ask=='1 kk' or ask=='1' or ask=='1kk':
                new='Euribor 1kk'
            elif ask=='3kk' or ask=='3' or ask=='3 kk':
                new='Euribor 3kk'
            elif ask=='6kk' or ask=='6' or ask=='6 kk': 
                new='Euribor 6kk'
            elif ask=='12kk' or ask=='12' or ask=='12 kk':
                new='Euribor 12kk'
            else:
                print(f'Euribor {ask} was not found')
        elif entry=='All' or entry=='all':
            new=column_titles
        return(new)
def graph(final):
    final=format(final)   
    fig=plt.figure(figsize=(12,7))
    plt.xlabel('Ajanjakso',fontsize=16)
    plt.ylabel('Korko',fontsize=16)
    if final==column_titles:
        title='Interest rates'
    else:
        title=final
    plt.title(f'{title} 1999-2021',fontsize=16)
    plt.plot(red[final])
    plt.xticks(red.index[::12],rotation=30)
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.savefig('Rate.png')
    photo= tk.PhotoImage(file='Rate.png')
    vlabel.configure(image=photo)
    vlabel.photo=photo
    vlabel.pack(side = "bottom",fill='both')
    print(final)

root = tk.Tk()

vlabel=tk.Label(root)
vlabel.pack()

canvas=tk.Canvas(root,height=Height,width=Width)
canvas.pack()

frame=tk.Frame(root,bg='#80c5ff',bd=4)
frame.place(relx=0.5,rely=0.1,relwidth=.75,relheight=.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',18))
entry.place(relwidth=0.65,relheight=1)


button=tk.Button(frame, text='Select interest rate',command=lambda: graph(entry.get()))
button.place(relx=.7,relwidth=.3,relheight=1)


root.mainloop()

