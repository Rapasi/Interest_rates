import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import pandas_datareader as pdr
import yfinance as yf
from datetime import datetime


Height=800
Width=1000

# Selected paths work only on my computers

path_lnx='~/Rami/Interest_rates/Interest_rates.xlsx'
path_windows=r'C:\Users\ramie\Downloads\korot.xlsx'

#lnx_stocks='~/Rami/Interest_rates\Kuvaaja_{0}.png'.format(i)
#save_fig_windows=r'C:\Users\ramie\Projects\Kuvaaja_{0}.png'.format(i)

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



start=datetime(2018,1,1)
end=datetime.today()
# Dimensions of document (not accurate currently)

WIDTH=210
HEIGHT=590

# List of stocks to plot

def get_name(osake_list):
    company_names=[]
    for name in osake_list:
        osake=yf.Ticker(name)
        company_name=osake.info['longName']
        company_names.append(company_name)
    return(company_names)

colours=['r','g','b','k','c','y','m','teal','sienna']
osakkeet=['ORTHEX.HE','WRT1V.HE','TYRES.HE','UPM.HE','METSB.HE','SHOT.ST','ZIGN.ST','OUT1V.HE','FIA1S.HE']
stock_names=get_name(osakkeet)

label_list = [
    pd.to_datetime("2021-07-21"),
    pd.to_datetime("2019-11-29"), 
    pd.to_datetime("2019-01-09"),
    (pd.to_datetime("2020-03-31"), pd.to_datetime("2019-06-27")),
    pd.to_datetime("2019-06-03"), 
    pd.to_datetime("2020-10-16"), 
    (pd.to_datetime("2021-01-04"), pd.to_datetime("2021-08-11")),
    (pd.to_datetime("2021-05-08"), pd.to_datetime("2019-02-13")),
    (pd.to_datetime("2020-06-11"), pd.to_datetime("2019-07-25"),pd.to_datetime("2018-11-27"))]

# Functions to download stock prices and plot graphs

def open_stock(Osake):
    osake=pdr.DataReader(Osake,'yahoo',start,end)
    hinta=osake['Adj Close']
    return(hinta)

my_stocks=open_stock(osakkeet)

def kuvaaja(Osake):
    ax=plt.gca()
    plt.close()
    plt.figure(figsize=(12,8))
    plt.plot(my_stocks[Osake])
    plt.xlabel('Aika',fontsize=14)
    plt.xticks(rotation=20)
    plt.title(stock_names[Osake],fontsize=18)
    plt.ylabel('Hinta',fontsize=14)
    plt.savefig('~/Rami/Interest_rates\Kuvaaja.png')
    # plt.figure(figsize=(12,8))
    # plt.xlabel('Aika',fontsize=14)
    # plt.title('All stocks',fontsize=18)
    # plt.ylabel('Hinta',fontsize=14)
    # plt.plot(open_stock(osakkeet))
    # plt.savefig(r'C:\Users\ramie\Projects\Kuvaaja_all.png')
    stock_img= tk.PhotoImage(file='Kuvaaja.png')
    vlabel.configure(image=stock_img)
    vlabel.photo=stock_img
    vlabel.pack(side = "bottom",fill='both')

def select_stock():
    selected_stock=drop_stocks.get()
    return(selected_stock)

def select_rate():
    selected_rate=variable.get()
    return(selected_rate)

root = tk.Tk()

drop_stocks=tk.StringVar(root)
drop_stocks.set('Stocks')
w=tk.OptionMenu(root,drop_stocks,*osakkeet)
w.pack(side='top')

stock_button=tk.Button(root, text='Select stocks',command=lambda: kuvaaja(open_stock(select_stock()))).pack()


vlabel=tk.Label(root)
vlabel.pack()
canvas=tk.Canvas(root,height=Height,width=Width)
canvas.pack()


variable=tk.StringVar(root)
variable.set('Interest rate')
w=tk.OptionMenu(root,variable,*column_titles,'All')
w.pack()



interest_button=tk.Button(root, text='Select interest rate',command=lambda: graph(select_rate())).pack()


root.mainloop()
