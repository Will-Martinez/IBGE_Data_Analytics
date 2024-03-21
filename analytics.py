import pandas as pd
import xlrd
import plotly.express as px

    
def StartAnalysis(xls_file):
    df = pd.read_excel(xls_file)

    # Cria um gráfico
    fig = px.bar(df, y='Alt.Geom. (h)', color='Região', hover_data=[
        'RN',
        'Estado',
        'Latitude',
        'Longitude',
        'Alt.Orto. (H)',
        'Alt.Geom. (h)',
        'SAT'
        ])

    # Adiciona titulo e labels para o gráfico
    fig.update_layout(title='Gráfico de altura geométrica por região',
                    xaxis_title='',
                    yaxis_title='Altura Geométrica (h)')

    # Mostra o gráfico
    fig.show()


def main():
    xls_file = "MAPGEO2015.xls"
    StartAnalysis(xls_file)

main()    