import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Configurando a página
st.set_page_config(
    page_title="Dashboard MUNIC",
    page_icon="dashboard_adidas/logoadidas.png",
    layout="wide",
)

paleta = ["#63A3B2", "#EF7158"]
amarelo = ["#FBD178"]
azul = ["#63A3B2"]
laranja = ['#EF7158']

# Função para calcular frequência relativa
def freq_rel(coluna):
    contagem = np.sum(coluna)
    calc = round((coluna / contagem) * 100, 2)
    return calc

st.title('Representatividade Feminina nos Órgãos Públicos Municipais')
geral, pre, edu, cul, esp, sau = st.tabs(["Geral", "Prefeituras", "Educação", "Cultura", "Esporte", "Saúde"])
#geral, pre, edu, cul, esp, sau = st.columns(6)

if geral:
    #st.markdown("""<br>""", unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])
    # Importando dados formatados
    df = pd.ExcelFile("Base_MUNIC_2021 - Atualizada.xlsx")


    # Nome das tabelas atuais
    df_planilhas = df.sheet_names
    # Importando cada planilha separadamente
    df_pre = pd.read_excel(df, sheet_name=df_planilhas[0])  # Informações atuais do prefeito
    df_edu = pd.read_excel(df, sheet_name=df_planilhas[1])  # Educação
    df_cul = pd.read_excel(df, sheet_name=df_planilhas[2])  # Cultura
    df_esp = pd.read_excel(df, sheet_name=df_planilhas[3])  # Esporte
    df_sau = pd.read_excel(df, sheet_name=df_planilhas[4])  # Saúde

    # Alterando nome das colunas
    dicionario_pre = df_pre.rename(
        columns={
            "Mun": "Municipio",
            "Mpeg02": "Mandato 2020",
            "Mpeg03": "Sexo",
            "Mpeg04": "Idade",
            "Mpeg05": "Raça",
            "Mpeg051": "Autodeclara",
            "Mpeg06": "Escolaridade",
            "Pop estimada 2021": "Pop",
        },
        inplace=True,
    )
    # Alterando valores da variável 'Regiao'
    mapeamento_pre = {
        "1 - Norte": "Norte",
        "2 - Nordeste": "Nordeste",
        "3 - Sudeste": "Sudeste",
        "4 - Sul": "Sul",
        "5 - Centro-Oeste": "Centro-Oeste",
    }
    df_pre["Regiao"] = df_pre["Regiao"].replace(mapeamento_pre)
    # Separando os sexos
    pre_fem = pd.DataFrame(df_pre[df_pre["Sexo"] == "Feminino"])
    pre_mas = pd.DataFrame(df_pre[df_pre["Sexo"] == "Masculino"])
    # Contando quantos prefeitos por sexo
    contagem_pre_fem = len(pre_fem)
    contagem_pre_mas = len(pre_mas)


    # Dados para o gráfico
    valores_pre = [contagem_pre_fem, contagem_pre_mas]
    rotulos_pre = ["Feminino", "Masculino"]

    with col1:

        st.write("Distribuição de Gênero nas Prefeituras")
        card1, card2 = st.columns([1,2])

        card1.metric(rotulos_pre[0], valores_pre[0])
        card2.metric(rotulos_pre[1], valores_pre[1])
        #st.markdown("""<br>""", unsafe_allow_html=True)
      
        figpie1 = px.pie(
        values=valores_pre,
        names=rotulos_pre,
        color_discrete_sequence=paleta,
        width=300,
        hole=0.5
        
    )
        st.plotly_chart(figpie1, use_container_width=False)

        # Agrupando escolaridade - Feminino
        escolaridade_pre_fem = pre_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_pre_fem['Percentagem'] = freq_rel(escolaridade_pre_fem['Frequência acumulada'])
        escolaridade_pre_fem = escolaridade_pre_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_pre_fem['Percentagem'] = escolaridade_pre_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_pre_fem = escolaridade_pre_fem.reset_index()

        st.write('Frequência do Nível Escolar das Prefeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_pre_fem[['Escolaridade', 'Percentagem']])

        
    # ---------------------------------------------------

    
    with col2:

        
        # Agrupando por estados
        uf_pre = pre_fem.groupby('UF').size().reset_index(name='Frequência acumulada')
        uf_pre['Frequência relativa'] = freq_rel(uf_pre['Frequência acumulada'])
        uf_pre = uf_pre.rename(columns={'UF': 'Estados'})
        uf_pre = uf_pre.sort_values(by='Frequência acumulada', ascending=False)
        uf_pre = uf_pre.reset_index()
        uf_pre = uf_pre.drop('index', axis=1)

        uf_pre_grafico = uf_pre[['Estados', 'Frequência acumulada']]
        uf_pre_rotulo = uf_pre['Frequência relativa'].apply(lambda x: f'{x:.2f}%')


        # Agrupando por região
        rg_pre = pre_fem.groupby('Regiao')['Regiao'].count().reset_index(name='Contagem')
        rg_pre['Percentagem'] = freq_rel(rg_pre['Contagem']).apply(lambda x: f'{x:.2f}%')
        rg_pre = rg_pre.reset_index().drop('index', axis=1).sort_values(by='Contagem', ascending=False)

        st.write('Frequência de Mulheres Prefeitas por Região', size=16)
        rg1, rg2, rg3, rg4, rg5 = st.columns(5)

        rg1.metric(rg_pre['Regiao'][0], rg_pre['Percentagem'][0])
        rg2.metric(rg_pre['Regiao'][1], rg_pre['Percentagem'][1])
        rg3.metric(rg_pre['Regiao'][2], rg_pre['Percentagem'][2])
        rg4.metric(rg_pre['Regiao'][3], rg_pre['Percentagem'][3])
        rg5.metric(rg_pre['Regiao'][4], rg_pre['Percentagem'][4])
        st.markdown("""<br>""", unsafe_allow_html=True)

        st.write('Frequência de Mulheres Prefeitas por Estado')
        figbar1 = px.bar(uf_pre,
            x='Estados',
            y='Frequência acumulada',
            #labels={'Frequência acumulada': 'Frequência Acumulada'},
            color_discrete_sequence=amarelo,
            width=900,
            height=390,
        )
        # Adicionando rótulos às barras
        figbar1.update_traces(
            text=uf_pre_rotulo, 
            textposition='outside', 
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(figbar1, use_container_width=False)

        graf1, graf2 = st.columns(2)
        
        # Dados de contagem de raça/paleta
        contagem_raca_paleta_pre = pre_fem['Raça'].value_counts().reset_index()
        contagem_raca_paleta_pre.columns = ['Raça/paleta', 'Contagem']

        # Dados de autodeclarações "Sim" por raça/paleta
        autodeclara_sim_pre = pre_fem[pre_fem['Autodeclara'] == 'Sim']
        contagem_autodeclara_sim_pre = autodeclara_sim_pre['Raça'].value_counts().reset_index()
        contagem_autodeclara_sim_pre.columns = ['Raça/paleta', 'Contagem']

        graf1.write('Classificação de Raça/Cor das Prefeitas')
        # Criar o gráfico de barras lado a lado
        figbar2 = px.bar(contagem_raca_paleta_pre, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/paleta', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=laranja
            )
        rotulo1 = contagem_raca_paleta_pre['Contagem']
        figbar2.update_traces(text=contagem_raca_paleta_pre['Contagem'], textposition='outside', showlegend=False)
        
        
        # Exibir o gráfico no Streamlit
        graf1.plotly_chart(figbar2, use_container_width=False)

        graf2.write('Prefeitas que falaram "Sim" para a classificação Étnico Racial')
        # Criar o gráfico de barras lado a lado
        figbar3 = px.bar(contagem_autodeclara_sim_pre, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/paleta', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_pre['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

        

        

# if pre:
#     st.markdown("""<br>""", unsafe_allow_html=True)
#     ...
# if edu:
#     st.markdown("""<br>""", unsafe_allow_html=True)
#     ...
# if cul:
#     st.markdown("""<br>""", unsafe_allow_html=True)

# if esp:
#     st.markdown("""<br>""", unsafe_allow_html=True)
#     ...
# if sau:
#     st.markdown("""<br>""", unsafe_allow_html=True)
#     ...