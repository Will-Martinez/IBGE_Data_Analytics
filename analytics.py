import pandas as pd
import xlrd
import plotly.express as px

df = pd.read_excel("MAPGEO2015.xls")
print(df.head())

# Criar gráfico de dispersão com Plotly
fig = px.bar(df, y='Alt.Geom. (h)', color='Região', hover_data=[
    'RN',
    'Estado',
    'Latitude',
    'Longitude',
    'Alt.Orto. (H)',
    'Alt.Geom. (h)',
    'SAT'
    ])

# Adicionar título e rótulos dos eixos
fig.update_layout(title='Gráfico de altura geométrica por região',
                  xaxis_title='',
                  yaxis_title='Altura Geométrica (h)')

# Mostrar o gráfico
fig.show()