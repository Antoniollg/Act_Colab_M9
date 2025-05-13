import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Datos simulados
df = pd.DataFrame({
    "equipo": ["Real Madrid", "Barcelona", "Atlético", "Sevilla"],
    "goles": [70, 65, 58, 50],
    "tiros": [300, 280, 260, 250]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Estadísticas de La Liga 2024"),

    dcc.Dropdown(
        id='equipo-dropdown',
        options=[{'label': i, 'value': i} for i in df['equipo']],
        value='Real Madrid'
    ),

    dcc.Graph(id='grafico-goles')
])

@app.callback(
    Output('grafico-goles', 'figure'),
    Input('equipo-dropdown', 'value')
)
def actualizar_grafico(equipo):
    fila = df[df['equipo'] == equipo]
    fig = px.bar(fila.melt(id_vars=["equipo"], value_vars=["goles", "tiros"]),
             x="variable", y="value", color="variable",
             labels={"variable": "Estadística", "value": "Valor"},
             title=f"Estadísticas de {equipo}")
    return fig

if __name__ == '__main__':
    app.run(debug=True)


