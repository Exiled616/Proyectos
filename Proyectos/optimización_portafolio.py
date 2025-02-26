import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
try:
    ruta = 'portfolio.xlsx'
    class Portafolio():
        cartera = pd.read_excel(ruta, index_col=0)
        cartera['Total ($)'] = cartera['Precio'] * cartera['Volumen'] 
        cartera
        total = round(cartera['Total ($)'].sum())
except:
    class Portafolio():
        cartera = pd.DataFrame({
            'Precio' : [12.01,245.67,368.45,137.96,155.43,46.42,416.4,462.80],
            'Volumen' : [2,0.6836,0.2573,0.3,0.3217,1.0807,0.0279,0.0273]
        }, index=['NU','AAPL','TSLA','NVDA','CVX', 'BAC', 'QQQ', 'BRKK.B'],
        )
        cartera['Total ($)'] = cartera['Precio'] * cartera['Volumen'] 
        total = round(cartera['Total ($)'].sum())
        # def exportar(self):
        #     self.cartera.to_excel('portafolio.xlsx')
    df_yf = yf.download(
        ['NU','AAPL','TSLA','NVDA','CVX', 'BAC'],
        period='360d',
        interval='1d',
        auto_adjust=False
    )
    df = df_yf[['Adj Close', 'Volume']]
    len(df.columns)
    df.columns[0][1]
    df.iloc(axis=1)[[0]]
    df.iloc(axis=1)[[0+6]]
    df.iloc(axis=1)[[11]]
    APPL = df.iloc(axis=1)[0] * df.iloc(axis=1)[6]
    print(APPL)
    range(round(len(df.columns)/2))
    for i in range(int(len(df.columns)/2)):
        df[('Market Cap', df.columns[i][1])] = df.iloc(axis=1)[i] * df.iloc(axis=1)[i+(round(len(df.columns)/2))]
    print(df[['Market Cap']])
    
        
