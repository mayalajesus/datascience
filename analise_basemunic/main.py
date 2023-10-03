import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
# Crie um aplicativo Dash
app = dash.Dash(__name__)

# Importando dados formatados
df = pd.ExcelFile("Base_MUNIC_2021 - Atualizada.xlsx")

# Nome das tabelas atuais
df_planilhas = df.sheet_names
# Importando cada planilha separadamente
df_pre = pd.read_excel(df, sheet_name=df_planilhas[0]) # Informações atuais do prefeito
df_edu = pd.read_excel(df, sheet_name=df_planilhas[1]) # Educação
df_cul = pd.read_excel(df, sheet_name=df_planilhas[2]) # Cultura
df_esp = pd.read_excel(df, sheet_name=df_planilhas[3]) # Esporte
df_sau = pd.read_excel(df, sheet_name=df_planilhas[4]) # Saúde
# Alterando nome das colunas
dicionario_pre = df_pre.rename (columns={ 'Mun': 'Municipio',
                  'Mpeg02': 'Mandato 2020',
                  'Mpeg03': 'Sexo',
                  'Mpeg04': 'Idade',
                  'Mpeg05': 'Raça',
                  'Mpeg051': 'Autodeclara',
                  'Mpeg06': 'Escolaridade',
                  'Pop estimada 2021': 'Pop'                      
}, inplace=True)
# Alterando valores da variável 'Regiao'
mapeamento_pre = {
    '1 - Norte': 'Norte',
    '2 - Nordeste': 'Nordeste',
    '3 - Sudeste': 'Sudeste',
    '4 - Sul': 'Sul',
    '5 - Centro-Oeste': 'Centro-Oeste',
}
df_pre['Regiao'] = df_pre['Regiao'].replace(mapeamento_pre)
# Separando os sexos
pre_fem =  pd.DataFrame(df_pre[df_pre['Sexo'] == 'Feminino'])
pre_mas =  pd.DataFrame(df_pre[df_pre['Sexo'] == 'Masculino'])
# Contando quantos prefeitos por sexo
contagem_pre_fem = len(pre_fem)
contagem_pre_mas = len(pre_mas)


# Dados para o gráfico
valores_pre = [contagem_pre_fem, contagem_pre_mas]
rotulos_pre = ['Feminino', 'Masculino']

# Defina o layout do aplicativo
app.layout = html.Div([
    dcc.Graph(
        id='grafico-pizza',
        figure={
            'data': [
                {
                    'values': valores_pre,
                    'labels': rotulos_pre,
                    'type': 'pie',
                    'marker': {'colors': ['#1967FF', '#AFFF59']},
                },
            ],
            'layout': {
                'title': 'Distribuição de Gênero',
                'titlefont': {'family': 'serif', 'color': '#1E1E1E', 'size': 12},
            },
        },
    ),
])




if __name__ == '__main__':
    app.run_server(debug=True)