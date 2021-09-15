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
new=''
def format(entry):
    if entry=='eonia' or entry=='Eonia':
        new='Eonia'
    elif entry=='Euribor 1kk':
        new='Euribor 1kk'
    elif entry=='Euribor 3kk':
        new='Euribor 3kk'
    elif entry=='Euribor 6kk':
        new='Euribor 6kk'
    elif entry=='Euribor 12kk':
        new='Euribor 12kk'
    elif entry=='All':
        new=column_titles
    else:
        print(f'{entry} was not a valid interest rate')
    return(new)


def graph(final):
    try:
        final=format(final)   
        fig=plt.figure(figsize=(12,7))
        plt.xlabel('Period',fontsize=16)
        plt.ylabel('Interest rate',fontsize=16)
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
    except Exception as e: 
        print(e)
        lower_frame=tk.Frame(root,bg='#80c5ff',bd=2)
        lower_frame.place(relx=0.4,rely=0.25,relwidth=.8,relheight=.15,anchor='n')
        label=tk.Label(lower_frame,font=('Courier',22),anchor='nw',justify='left',bd=4,text='Unable to draw graphs. Please check spelling.')
        label.place(relwidth=1,relheight=1)


root = tk.Tk()

vlabel=tk.Label(root)
vlabel.pack()

canvas=tk.Canvas(root,height=Height,width=Width)
canvas.pack()


variable=tk.StringVar(root)
variable.set('Interest rate')
w=tk.OptionMenu(root,variable,*column_titles,'All')
w.pack()

def select():
    selected=variable.get()
    return(selected)

button=tk.Button(root, text='Select interest rate',command=lambda: graph(select())).pack()


root.mainloop()
