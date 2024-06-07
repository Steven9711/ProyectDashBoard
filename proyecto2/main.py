import streamsync as ss
import pandas as pd
import plotly.express as px
import numpy as np

data_link = "https://raw.githubusercontent.com/cgl-itm/ProgramacionAvanzada-ITM/main/Proyectos/04_Datos/02_london_weather.csv"
data = pd.read_csv(data_link, index_col=0, parse_dates=True)

def update(state):
    if state["column"] in data.columns:
        df = data[state["column"]]
        state["graficol"] = px.line(df)
        state["grafiHist"]=px.histogram(df)
        state["medVar"]="{:.2f}".format(df.mean())
        state["minVar"]="{:.2f}".format(df.min())
        state["maxVar"]="{:.2f}".format(df.max())
        state["desVar"]="{:.2f}".format(df.std())

def updateBi(state):
    df = data[state["fecha_ini"]:state["fecha_fin"]] 
    if state["column"] in df.columns and state["column1"] in df.columns:
        corr = df[state['column']].corr(df[state['column1']])
        state["Corvar"] = "{:.7f}".format(corr) 
        state["graficScatter"] = px.scatter(df,x=state['column'], y=state['column1'])

def updateBox(state):
    df = data[data.index.month == int(state['mes'])]
    if state["column"] in df.columns:
        state["graficoBox"] = px.box(df, x=df.index.year, y=state['column'])
    
initial_state = ss.init_state({
    "my_app": {
        "title": "Dashboard"
    },
    "dataframe": data,
    "var":{str(key):str(key) for key in data.columns},
    "var2":{str(key):str(key) for key in data.columns},
    "column":'cloud_cover',
    "column1":'cloud_cover',
    "graficol": None,
    "grafiHist":None,
    "medVar":0.0,
    "minVar":0.0,
    "maxVar":0.0,
    "desVar":0.0,
    "fecha_ini": data.index.min().date(),
    "fecha_fin": data.index.max().date(),
    "meses": {str(k):str(k) for k in range(1,13)},
    "mes": '1',
    "graficoBox": None,
    "graficScatter"
    "graficoCor" : None,
    "Corvar":0.0,
    
  
})
update(initial_state)
updateBi(initial_state)
updateBox(initial_state)
