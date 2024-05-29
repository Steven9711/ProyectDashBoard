import streamsync as ss
import pandas as pd
import plotly.express as px

data_link = "https://raw.githubusercontent.com/cgl-itm/ProgramacionAvanzada-ITM/main/Proyectos/04_Datos/02_london_weather.csv"
data = pd.read_csv(data_link, index_col=0, parse_dates=True)

def update(state):
    df = data[state["column"]]
    state["graficol"] = px.line(df)
    state["grafiHist"]=px.histogram(df)
    state["medVar"]="{:.2f}".format(df.mean())
    state["minVar"]="{:.2f}".format(df.min().round(3))
    state["maxVar"]="{:.2f}".format(df.max().round(3))
    state["desVar"]="{:.2f}".format(df.std().round(3))

def updateBi(state):
    print(type(state["fecha_ini"]),type(state["fecha_fin"]))
    df = data[state["fecha_ini"]:state["fecha_fin"]]    

def updateBox(state):
    df = data[state["column"]]
    #df = data[data.index.month == int(state['selMonth'])]
    #dataDeads1=data.loc[data['Survived']==1,['Survived','Sex']].groupby(by='Sex').count()
    dataDate=data[df].groupby(by=([data.index.month, data.index.year]))
    state["graficoBox"] = px.box(dataDate, x=df.index.year,y="column")

initial_state = ss.init_state({
    "my_app": {
        "title": "My App"
    },
    "dataframe": data,
    "var":{str(key):str(key) for key in data.columns},
    "column":'cloud_cover',
    "graficol": None,
    "grafiHist":None,
    "medVar":0.0,
    "minVar":0.0,
    "maxVar":0.0,
    "desVar":0.0,
    "fecha_ini": data.index.min().date(),
    "fecha_fin": data.index.max().date(),
    "monthsInData": {str(k):str(k) for k in range(1,13)},
    "selMonth": '1',
    
  
})
update(initial_state)
updateBi(initial_state)
updateBox(initial_state)
