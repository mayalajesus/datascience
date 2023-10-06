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

# ----------------------------------------------------------------------

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



# Alterando nome das colunas
dicionario_edu = df_edu.rename (columns={ 'Mun': 'Municipio',
                  'Medu01': 'Orgao Gestor',
                  'Medu03': 'Sexo',
                  'Medu04': 'Idade',
                  'Medu05': 'Raça',
                  'Medu051': 'Autodeclara',
                  'Medu06': 'Escolaridade'
}, inplace=True)

# Alterando valores da coluna 'Regiao'
mapeamento_edu = {
    '1 - Norte': 'Norte',
    '2 - Nordeste': 'Nordeste',
    '3 - Sudeste': 'Sudeste',
    '4 - Sul': 'Sul',
    '5 - Centro-Oeste': 'Centro-Oeste',
}
df_edu['Regiao'] = df_edu['Regiao'].replace(mapeamento_edu)



# Alterando nome das colunas
dicionario_cul = df_cul.rename (columns={ 'Mun': 'Municipio',
                  'Mcul01': 'Orgao Gestor',
                  'Mcul03': 'Sexo',
                  'Mcul04': 'Idade',
                  'Mcul05': 'Raça',
                  'Mcul051': 'Autodeclara',
                  'Mcul06': 'Escolaridade'
}, inplace=True)

# Alterando valores da coluna 'Regiao'
mapeamento_cul = {
    '1 - Norte': 'Norte',
    '2 - Nordeste': 'Nordeste',
    '3 - Sudeste': 'Sudeste',
    '4 - Sul': 'Sul',
    '5 - Centro-Oeste': 'Centro-Oeste',
}
df_cul['Regiao'] = df_cul['Regiao'].replace(mapeamento_cul)


# Alterando nome das colunas
dicionario_esp = df_esp.rename (columns={ 'Mun': 'Municipio',
                  'Mesp01': 'Orgao Gestor',
                  'Mesp03': 'Sexo',
                  'Mesp04': 'Idade',
                  'Mesp05': 'Raça',
                  'Mesp051': 'Autodeclara',
                  'Mesp06': 'Escolaridade'
}, inplace=True)

# Alterando valores da coluna 'Regiao'
mapeamento_esp = {
    '1 - Norte': 'Norte',
    '2 - Nordeste': 'Nordeste',
    '3 - Sudeste': 'Sudeste',
    '4 - Sul': 'Sul',
    '5 - Centro-Oeste': 'Centro-Oeste',
}
df_esp['Regiao'] = df_esp['Regiao'].replace(mapeamento_esp)

# Alterando nome das colunas
dicionario_sau = df_sau.rename (columns={ 'Mun': 'Municipio',
                  'Msau01': 'Orgao Gestor',
                  'Msau03': 'Sexo',
                  'Msau04': 'Idade',
                  'Msau05': 'Raça',
                  'Msau051': 'Autodeclara',
                  'Msau06': 'Escolaridade'
}, inplace=True)

# Alterando valores da coluna 'Regiao'
mapeamento_sau = {
    '1 - Norte': 'Norte',
    '2 - Nordeste': 'Nordeste',
    '3 - Sudeste': 'Sudeste',
    '4 - Sul': 'Sul',
    '5 - Centro-Oeste': 'Centro-Oeste',
}
df_sau['Regiao'] = df_sau['Regiao'].replace(mapeamento_sau)


# ----------------------------------------------------------------------


st.title('Representatividade Feminina nos Órgãos Públicos Municipais')

# Usando guias para navegar entre as páginas
tabs = st.tabs(["Geral", "Prefeituras", "Educação", "Cultura", "Esporte", "Saúde"])

# ----------------------------------------------------------------------

with tabs[0]:
    st.markdown("""<br>""", unsafe_allow_html=True)

    colge1,colge2 = st.columns(2)

    with colge1:

        # Separando os sexos
        pre_fem =  pd.DataFrame(df_pre[df_pre['Sexo'] == 'Feminino'])
        pre_mas =  pd.DataFrame(df_pre[df_pre['Sexo'] == 'Masculino'])
        # Contando quantos prefeitos por sexo
        contagem_pre_fem = len(pre_fem)
        contagem_pre_mas = len(pre_mas)

        # Separando os sexos
        edu_fem = pd.DataFrame(df_edu[df_edu['Sexo'] == 'Feminino'])
        edu_mas = pd.DataFrame(df_edu[df_edu['Sexo'] == 'Masculino'])
        # Contagem
        contagem_edu_fem = len(edu_fem)
        contagem_edu_mas = len(edu_mas)

        # Separando os sexos
        cul_fem = pd.DataFrame(df_cul[df_cul['Sexo'] == 'Feminino'])
        cul_mas = pd.DataFrame(df_cul[df_cul['Sexo'] == 'Masculino'])
        # Contagem
        contagem_cul_fem = len(cul_fem)
        contagem_cul_mas = len(cul_mas)

        # Separando os sexos
        esp_fem = pd.DataFrame(df_esp[df_esp['Sexo'] == 'Feminino'])
        esp_mas = pd.DataFrame(df_esp[df_esp['Sexo'] == 'Masculino'])
        # Contagem
        contagem_esp_fem = len(esp_fem)
        contagem_esp_mas = len(esp_mas)

        # Separando os sexos
        sau_fem = pd.DataFrame(df_sau[df_sau['Sexo'] == 'Feminino'])
        sau_mas = pd.DataFrame(df_sau[df_sau['Sexo'] == 'Masculino'])
        # Contagem
        contagem_sau_fem = len(sau_fem)
        contagem_sau_mas = len(sau_mas)
                        
        # Feminino
        geral_fem = (contagem_pre_fem, contagem_edu_fem, contagem_cul_fem, contagem_esp_fem, contagem_sau_fem)
        contagem_geral_fem = np.sum(geral_fem)

        # Masculino
        geral_mas = (contagem_pre_mas, contagem_edu_mas, contagem_cul_mas, contagem_esp_mas, contagem_sau_mas)
        contagem_geral_mas = np.sum(geral_mas)

        # Dados
        labels = ["Feminino", "Masculino"]
        valores = [contagem_geral_fem, contagem_geral_mas]

        # Criar a figura de pizza
        fig_pizza = px.pie(
            names=labels,
            values=valores,
            title="Distribuição de Gênero Geral",
            width=400,
            hole=0.5
        )

        # Exibir a figura no Streamlit
        st.plotly_chart(fig_pizza, use_container_width=True)

    with colge2:
        pre_fem = pd.DataFrame(df_pre[df_pre["Sexo"] == "Feminino"])
        edu_fem = pd.DataFrame(df_edu[df_edu["Sexo"] == "Feminino"])
        cul_fem = pd.DataFrame(df_cul[df_cul["Sexo"] == "Feminino"])
        esp_fem = pd.DataFrame(df_esp[df_esp["Sexo"] == "Feminino"])
        sau_fem = pd.DataFrame(df_sau[df_sau["Sexo"] == "Feminino"])
        geral_fem = pd.concat([pre_fem, edu_fem, cul_fem, esp_fem, sau_fem])
        geral_fem.drop(columns=['Faixa_pop'], inplace=True)

        dados = geral_fem['Pop']

        intervalos = [
            (0, 5000),
            (5001, 10000),
            (10001, 20000),
            (20001, 50000),
            (50001, 100000),
            (100001, 500000),
            (500001, max(dados))
        ]

        def atribuir_faixa_populacional(valor):
            for i, (min_intervalo, max_intervalo) in enumerate(intervalos):
                if min_intervalo <= valor <= max_intervalo:
                    return f"{min_intervalo} - {max_intervalo}"

        geral_fem['Faixa Populacional'] = geral_fem['Pop'].apply(atribuir_faixa_populacional)

        contagem_faixa_populacional = geral_fem['Faixa Populacional'].value_counts().reset_index()
        contagem_faixa_populacional.columns = ['Faixa Populacional', 'Contagem']
        
        st.write("Faixa Populacional nas Cidades com Liderança Feminina")
        figpop = px.bar(contagem_faixa_populacional, x='Faixa Populacional', y='Contagem',
                    labels={'Faixa Populacional': 'Faixa Populacional', 'Contagem': 'Contagem'},
                    color_discrete_sequence=laranja
                    )
        
        figpop.update_traces(
            text=contagem_faixa_populacional['Contagem'], 
            textposition='outside', 
        )

        st.plotly_chart(figpop, use_container_width=True)

# ----------------------------------------------------------------------

with tabs[1]:
    colpre1, colpre2 = st.columns([1,2])

    with colpre1:
        st.markdown("""<br>""", unsafe_allow_html=True)

        pre_fem = pd.DataFrame(df_pre[df_pre["Sexo"] == "Feminino"])

        contagem_pre_fem = len(pre_fem)

        valores_pre = [contagem_pre_fem, len(df_pre) - contagem_pre_fem]
        rotulos_pre = ["Feminino", "Masculino"]

        st.write("Distribuição de Gênero nas Prefeituras")
        card1, card2 = st.columns([1, 2])

        card1.metric(rotulos_pre[0], valores_pre[0])
        card2.metric(rotulos_pre[1], valores_pre[1])

        figpie1 = px.pie(
            values=valores_pre,
            names=rotulos_pre,
            color_discrete_sequence=paleta,
            width=400,
            hole=0.5
        )
        st.plotly_chart(figpie1, use_container_width=False)

        escolaridade_pre_fem = pre_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_pre_fem['Percentagem'] = freq_rel(escolaridade_pre_fem['Frequência acumulada'])
        escolaridade_pre_fem = escolaridade_pre_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_pre_fem['Percentagem'] = escolaridade_pre_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_pre_fem = escolaridade_pre_fem.reset_index()

        st.write('Frequência do Nível Escolar das Prefeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_pre_fem[['Escolaridade', 'Percentagem']])
    with colpre2:    
        colpre = st.columns(2)
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
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
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
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_pre['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

# ----------------------------------------------------------------------

with tabs[2]:
    coledu1, coledu2 = st.columns([1,2])

    with coledu1:
        st.markdown("""<br>""", unsafe_allow_html=True)

        edu_fem = pd.DataFrame(df_edu[df_edu["Sexo"] == "Feminino"])

        contagem_edu_fem = len(edu_fem)

        valores_edu = [contagem_edu_fem, len(df_edu) - contagem_edu_fem]
        rotulos_edu = ["Feminino", "Masculino"]

        st.write("Distribuição de Gênero nas edufeituras")
        card1, card2 = st.columns([1, 2])

        card1.metric(rotulos_edu[0], valores_edu[0])
        card2.metric(rotulos_edu[1], valores_edu[1])

        figpie1 = px.pie(
            values=valores_edu,
            names=rotulos_edu,
            color_discrete_sequence=paleta,
            width=400,
            hole=0.5
        )
        st.plotly_chart(figpie1, use_container_width=False)

        escolaridade_edu_fem = edu_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_edu_fem['Percentagem'] = freq_rel(escolaridade_edu_fem['Frequência acumulada'])
        escolaridade_edu_fem = escolaridade_edu_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_edu_fem['Percentagem'] = escolaridade_edu_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_edu_fem = escolaridade_edu_fem.reset_index()

        st.write('Frequência do Nível Escolar das edufeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_edu_fem[['Escolaridade', 'Percentagem']])
    with coledu2:    
        coledu = st.columns(2)
        # Agrupando por estados
        uf_edu = edu_fem.groupby('UF').size().reset_index(name='Frequência acumulada')
        uf_edu['Frequência relativa'] = freq_rel(uf_edu['Frequência acumulada'])
        uf_edu = uf_edu.rename(columns={'UF': 'Estados'})
        uf_edu = uf_edu.sort_values(by='Frequência acumulada', ascending=False)
        uf_edu = uf_edu.reset_index()
        uf_edu = uf_edu.drop('index', axis=1)

        uf_edu_grafico = uf_edu[['Estados', 'Frequência acumulada']]
        uf_edu_rotulo = uf_edu['Frequência relativa'].apply(lambda x: f'{x:.2f}%')


        # Agrupando por região
        rg_edu = edu_fem.groupby('Regiao')['Regiao'].count().reset_index(name='Contagem')
        rg_edu['Percentagem'] = freq_rel(rg_edu['Contagem']).apply(lambda x: f'{x:.2f}%')
        rg_edu = rg_edu.reset_index().drop('index', axis=1).sort_values(by='Contagem', ascending=False)

        st.write('Frequência de Mulheres edufeitas por Região', size=16)
        rg1, rg2, rg3, rg4, rg5 = st.columns(5)

        rg1.metric(rg_edu['Regiao'][0], rg_edu['Percentagem'][0])
        rg2.metric(rg_edu['Regiao'][1], rg_edu['Percentagem'][1])
        rg3.metric(rg_edu['Regiao'][2], rg_edu['Percentagem'][2])
        rg4.metric(rg_edu['Regiao'][3], rg_edu['Percentagem'][3])
        rg5.metric(rg_edu['Regiao'][4], rg_edu['Percentagem'][4])
        st.markdown("""<br>""", unsafe_allow_html=True)

        st.write('Frequência de Mulheres edufeitas por Estado')
        figbar1 = px.bar(uf_edu,
            x='Estados',
            y='Frequência acumulada',
            #labels={'Frequência acumulada': 'Frequência Acumulada'},
            color_discrete_sequence=amarelo,
            width=900,
            height=390,
        )
        # Adicionando rótulos às barras
        figbar1.update_traces(
            text=uf_edu_rotulo, 
            textposition='outside', 
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(figbar1, use_container_width=False)

        graf1, graf2 = st.columns(2)
        
        # Dados de contagem de raça/paleta
        contagem_raca_paleta_edu = edu_fem['Raça'].value_counts().reset_index()
        contagem_raca_paleta_edu.columns = ['Raça/paleta', 'Contagem']

        # Dados de autodeclarações "Sim" por raça/paleta
        autodeclara_sim_edu = edu_fem[edu_fem['Autodeclara'] == 'Sim']
        contagem_autodeclara_sim_edu = autodeclara_sim_edu['Raça'].value_counts().reset_index()
        contagem_autodeclara_sim_edu.columns = ['Raça/paleta', 'Contagem']

        graf1.write('Classificação de Raça/Cor das edufeitas')
        # Criar o gráfico de barras lado a lado
        figbar2 = px.bar(contagem_raca_paleta_edu, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=laranja
            )
        rotulo1 = contagem_raca_paleta_edu['Contagem']
        figbar2.update_traces(text=contagem_raca_paleta_edu['Contagem'], textposition='outside', showlegend=False)
        
        
        # Exibir o gráfico no Streamlit
        graf1.plotly_chart(figbar2, use_container_width=False)

        graf2.write('edufeitas que falaram "Sim" para a classificação Étnico Racial')
        # Criar o gráfico de barras lado a lado
        figbar3 = px.bar(contagem_autodeclara_sim_edu, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_edu['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

# ----------------------------------------------------------------------

with tabs[3]:
    colcul1, colcul2 = st.columns([1,2])

    with colcul1:
        st.markdown("""<br>""", unsafe_allow_html=True)

        cul_fem = pd.DataFrame(df_cul[df_cul["Sexo"] == "Feminino"])

        contagem_cul_fem = len(cul_fem)

        valores_cul = [contagem_cul_fem, len(df_cul) - contagem_cul_fem]
        rotulos_cul = ["Feminino", "Masculino"]

        st.write("Distribuição de Gênero nas culfeituras")
        card1, card2 = st.columns([1, 2])

        card1.metric(rotulos_cul[0], valores_cul[0])
        card2.metric(rotulos_cul[1], valores_cul[1])

        figpie1 = px.pie(
            values=valores_cul,
            names=rotulos_cul,
            color_discrete_sequence=paleta,
            width=400,
            hole=0.5
        )
        st.plotly_chart(figpie1, use_container_width=False)

        escolaridade_cul_fem = cul_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_cul_fem['Percentagem'] = freq_rel(escolaridade_cul_fem['Frequência acumulada'])
        escolaridade_cul_fem = escolaridade_cul_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_cul_fem['Percentagem'] = escolaridade_cul_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_cul_fem = escolaridade_cul_fem.reset_index()

        st.write('Frequência do Nível Escolar das culfeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_cul_fem[['Escolaridade', 'Percentagem']])
    with colcul2:    
        colcul = st.columns(2)
        # Agrupando por estados
        uf_cul = cul_fem.groupby('UF').size().reset_index(name='Frequência acumulada')
        uf_cul['Frequência relativa'] = freq_rel(uf_cul['Frequência acumulada'])
        uf_cul = uf_cul.rename(columns={'UF': 'Estados'})
        uf_cul = uf_cul.sort_values(by='Frequência acumulada', ascending=False)
        uf_cul = uf_cul.reset_index()
        uf_cul = uf_cul.drop('index', axis=1)

        uf_cul_grafico = uf_cul[['Estados', 'Frequência acumulada']]
        uf_cul_rotulo = uf_cul['Frequência relativa'].apply(lambda x: f'{x:.2f}%')


        # Agrupando por região
        rg_cul = cul_fem.groupby('Regiao')['Regiao'].count().reset_index(name='Contagem')
        rg_cul['Percentagem'] = freq_rel(rg_cul['Contagem']).apply(lambda x: f'{x:.2f}%')
        rg_cul = rg_cul.reset_index().drop('index', axis=1).sort_values(by='Contagem', ascending=False)

        st.write('Frequência de Mulheres culfeitas por Região', size=16)
        rg1, rg2, rg3, rg4, rg5 = st.columns(5)

        rg1.metric(rg_cul['Regiao'][0], rg_cul['Percentagem'][0])
        rg2.metric(rg_cul['Regiao'][1], rg_cul['Percentagem'][1])
        rg3.metric(rg_cul['Regiao'][2], rg_cul['Percentagem'][2])
        rg4.metric(rg_cul['Regiao'][3], rg_cul['Percentagem'][3])
        rg5.metric(rg_cul['Regiao'][4], rg_cul['Percentagem'][4])
        st.markdown("""<br>""", unsafe_allow_html=True)

        st.write('Frequência de Mulheres culfeitas por Estado')
        figbar1 = px.bar(uf_cul,
            x='Estados',
            y='Frequência acumulada',
            #labels={'Frequência acumulada': 'Frequência Acumulada'},
            color_discrete_sequence=amarelo,
            width=900,
            height=390,
        )
        # Adicionando rótulos às barras
        figbar1.update_traces(
            text=uf_cul_rotulo, 
            textposition='outside', 
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(figbar1, use_container_width=False)

        graf1, graf2 = st.columns(2)
        
        # Dados de contagem de raça/paleta
        contagem_raca_paleta_cul = cul_fem['Raça'].value_counts().reset_index()
        contagem_raca_paleta_cul.columns = ['Raça/paleta', 'Contagem']

        # Dados de autodeclarações "Sim" por raça/paleta
        autodeclara_sim_cul = cul_fem[cul_fem['Autodeclara'] == 'Sim']
        contagem_autodeclara_sim_cul = autodeclara_sim_cul['Raça'].value_counts().reset_index()
        contagem_autodeclara_sim_cul.columns = ['Raça/paleta', 'Contagem']

        graf1.write('Classificação de Raça/Cor das culfeitas')
        # Criar o gráfico de barras lado a lado
        figbar2 = px.bar(contagem_raca_paleta_cul, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=laranja
            )
        rotulo1 = contagem_raca_paleta_cul['Contagem']
        figbar2.update_traces(text=contagem_raca_paleta_cul['Contagem'], textposition='outside', showlegend=False)
        
        
        # Exibir o gráfico no Streamlit
        graf1.plotly_chart(figbar2, use_container_width=False)

        graf2.write('culfeitas que falaram "Sim" para a classificação Étnico Racial')
        # Criar o gráfico de barras lado a lado
        figbar3 = px.bar(contagem_autodeclara_sim_cul, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_cul['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

# ----------------------------------------------------------------------

with tabs[4]:
    colesp1, colesp2 = st.columns([1,2])

    with colesp1:
        st.markdown("""<br>""", unsafe_allow_html=True)

        esp_fem = pd.DataFrame(df_esp[df_esp["Sexo"] == "Feminino"])

        contagem_esp_fem = len(esp_fem)

        valores_esp = [contagem_esp_fem, len(df_esp) - contagem_esp_fem]
        rotulos_esp = ["Feminino", "Masespino"]

        st.write("Distribuição de Gênero nas espfeituras")
        card1, card2 = st.columns([1, 2])

        card1.metric(rotulos_esp[0], valores_esp[0])
        card2.metric(rotulos_esp[1], valores_esp[1])

        figpie1 = px.pie(
            values=valores_esp,
            names=rotulos_esp,
            color_discrete_sequence=paleta,
            width=400,
            hole=0.5
        )
        st.plotly_chart(figpie1, use_container_width=False)

        escolaridade_esp_fem = esp_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_esp_fem['Percentagem'] = freq_rel(escolaridade_esp_fem['Frequência acumulada'])
        escolaridade_esp_fem = escolaridade_esp_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_esp_fem['Percentagem'] = escolaridade_esp_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_esp_fem = escolaridade_esp_fem.reset_index()

        st.write('Frequência do Nível Escolar das espfeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_esp_fem[['Escolaridade', 'Percentagem']])
    with colesp2:    
        colesp = st.columns(2)
        # Agrupando por estados
        uf_esp = esp_fem.groupby('UF').size().reset_index(name='Frequência acumulada')
        uf_esp['Frequência relativa'] = freq_rel(uf_esp['Frequência acumulada'])
        uf_esp = uf_esp.rename(columns={'UF': 'Estados'})
        uf_esp = uf_esp.sort_values(by='Frequência acumulada', ascending=False)
        uf_esp = uf_esp.reset_index()
        uf_esp = uf_esp.drop('index', axis=1)

        uf_esp_grafico = uf_esp[['Estados', 'Frequência acumulada']]
        uf_esp_rotulo = uf_esp['Frequência relativa'].apply(lambda x: f'{x:.2f}%')


        # Agrupando por região
        rg_esp = esp_fem.groupby('Regiao')['Regiao'].count().reset_index(name='Contagem')
        rg_esp['Percentagem'] = freq_rel(rg_esp['Contagem']).apply(lambda x: f'{x:.2f}%')
        rg_esp = rg_esp.reset_index().drop('index', axis=1).sort_values(by='Contagem', ascending=False)

        st.write('Frequência de Mulheres espfeitas por Região', size=16)
        rg1, rg2, rg3, rg4, rg5 = st.columns(5)

        rg1.metric(rg_esp['Regiao'][0], rg_esp['Percentagem'][0])
        rg2.metric(rg_esp['Regiao'][1], rg_esp['Percentagem'][1])
        rg3.metric(rg_esp['Regiao'][2], rg_esp['Percentagem'][2])
        rg4.metric(rg_esp['Regiao'][3], rg_esp['Percentagem'][3])
        rg5.metric(rg_esp['Regiao'][4], rg_esp['Percentagem'][4])
        st.markdown("""<br>""", unsafe_allow_html=True)

        st.write('Frequência de Mulheres espfeitas por Estado')
        figbar1 = px.bar(uf_esp,
            x='Estados',
            y='Frequência acumulada',
            #labels={'Frequência acumulada': 'Frequência Acumulada'},
            color_discrete_sequence=amarelo,
            width=900,
            height=390,
        )
        # Adicionando rótulos às barras
        figbar1.update_traces(
            text=uf_esp_rotulo, 
            textposition='outside', 
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(figbar1, use_container_width=False)

        graf1, graf2 = st.columns(2)
        
        # Dados de contagem de raça/paleta
        contagem_raca_paleta_esp = esp_fem['Raça'].value_counts().reset_index()
        contagem_raca_paleta_esp.columns = ['Raça/paleta', 'Contagem']

        # Dados de autodeclarações "Sim" por raça/paleta
        autodeclara_sim_esp = esp_fem[esp_fem['Autodeclara'] == 'Sim']
        contagem_autodeclara_sim_esp = autodeclara_sim_esp['Raça'].value_counts().reset_index()
        contagem_autodeclara_sim_esp.columns = ['Raça/paleta', 'Contagem']

        graf1.write('Classificação de Raça/Cor das espfeitas')
        # Criar o gráfico de barras lado a lado
        figbar2 = px.bar(contagem_raca_paleta_esp, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=laranja
            )
        rotulo1 = contagem_raca_paleta_esp['Contagem']
        figbar2.update_traces(text=contagem_raca_paleta_esp['Contagem'], textposition='outside', showlegend=False)
        
        
        # Exibir o gráfico no Streamlit
        graf1.plotly_chart(figbar2, use_container_width=False)

        graf2.write('espfeitas que falaram "Sim" para a classificação Étnico Racial')
        # Criar o gráfico de barras lado a lado
        figbar3 = px.bar(contagem_autodeclara_sim_esp, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_esp['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

# ----------------------------------------------------------------------

with tabs[5]:
    colsau1, colsau2 = st.columns([1,2])

    with colsau1:
        st.markdown("""<br>""", unsafe_allow_html=True)

        sau_fem = pd.DataFrame(df_sau[df_sau["Sexo"] == "Feminino"])

        contagem_sau_fem = len(sau_fem)

        valores_sau = [contagem_sau_fem, len(df_sau) - contagem_sau_fem]
        rotulos_sau = ["Feminino", "Massauino"]

        st.write("Distribuição de Gênero nas saufeituras")
        card1, card2 = st.columns([1, 2])

        card1.metric(rotulos_sau[0], valores_sau[0])
        card2.metric(rotulos_sau[1], valores_sau[1])

        figpie1 = px.pie(
            values=valores_sau,
            names=rotulos_sau,
            color_discrete_sequence=paleta,
            width=400,
            hole=0.5
        )
        st.plotly_chart(figpie1, use_container_width=False)

        escolaridade_sau_fem = sau_fem.groupby('Escolaridade')['Escolaridade'].count().reset_index(name='Frequência acumulada')
        escolaridade_sau_fem['Percentagem'] = freq_rel(escolaridade_sau_fem['Frequência acumulada'])
        escolaridade_sau_fem = escolaridade_sau_fem.reset_index().drop('index', axis=1).sort_values(by='Percentagem', ascending=False)
        escolaridade_sau_fem['Percentagem'] = escolaridade_sau_fem['Percentagem'].apply(lambda x: f'{x:.2f}%')
        escolaridade_sau_fem = escolaridade_sau_fem.reset_index()

        st.write('Frequência do Nível Escolar das saufeitas')
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.dataframe(escolaridade_sau_fem[['Escolaridade', 'Percentagem']])
    with colsau2:    
        colsau = st.columns(2)
        # Agrupando por estados
        uf_sau = sau_fem.groupby('UF').size().reset_index(name='Frequência acumulada')
        uf_sau['Frequência relativa'] = freq_rel(uf_sau['Frequência acumulada'])
        uf_sau = uf_sau.rename(columns={'UF': 'Estados'})
        uf_sau = uf_sau.sort_values(by='Frequência acumulada', ascending=False)
        uf_sau = uf_sau.reset_index()
        uf_sau = uf_sau.drop('index', axis=1)

        uf_sau_grafico = uf_sau[['Estados', 'Frequência acumulada']]
        uf_sau_rotulo = uf_sau['Frequência relativa'].apply(lambda x: f'{x:.2f}%')


        # Agrupando por região
        rg_sau = sau_fem.groupby('Regiao')['Regiao'].count().reset_index(name='Contagem')
        rg_sau['Percentagem'] = freq_rel(rg_sau['Contagem']).apply(lambda x: f'{x:.2f}%')
        rg_sau = rg_sau.reset_index().drop('index', axis=1).sort_values(by='Contagem', ascending=False)

        st.write('Frequência de Mulheres saufeitas por Região', size=16)
        rg1, rg2, rg3, rg4, rg5 = st.columns(5)

        rg1.metric(rg_sau['Regiao'][0], rg_sau['Percentagem'][0])
        rg2.metric(rg_sau['Regiao'][1], rg_sau['Percentagem'][1])
        rg3.metric(rg_sau['Regiao'][2], rg_sau['Percentagem'][2])
        rg4.metric(rg_sau['Regiao'][3], rg_sau['Percentagem'][3])
        rg5.metric(rg_sau['Regiao'][4], rg_sau['Percentagem'][4])
        st.markdown("""<br>""", unsafe_allow_html=True)

        st.write('Frequência de Mulheres saufeitas por Estado')
        figbar1 = px.bar(uf_sau,
            x='Estados',
            y='Frequência acumulada',
            #labels={'Frequência acumulada': 'Frequência Acumulada'},
            color_discrete_sequence=amarelo,
            width=900,
            height=390,
        )
        # Adicionando rótulos às barras
        figbar1.update_traces(
            text=uf_sau_rotulo, 
            textposition='outside', 
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(figbar1, use_container_width=False)

        graf1, graf2 = st.columns(2)
        
        # Dados de contagem de raça/paleta
        contagem_raca_paleta_sau = sau_fem['Raça'].value_counts().reset_index()
        contagem_raca_paleta_sau.columns = ['Raça/paleta', 'Contagem']

        # Dados de autodeclarações "Sim" por raça/paleta
        autodeclara_sim_sau = sau_fem[sau_fem['Autodeclara'] == 'Sim']
        contagem_autodeclara_sim_sau = autodeclara_sim_sau['Raça'].value_counts().reset_index()
        contagem_autodeclara_sim_sau.columns = ['Raça/paleta', 'Contagem']

        graf1.write('Classificação de Raça/Cor das saufeitas')
        # Criar o gráfico de barras lado a lado
        figbar2 = px.bar(contagem_raca_paleta_sau, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=laranja
            )
        rotulo1 = contagem_raca_paleta_sau['Contagem']
        figbar2.update_traces(text=contagem_raca_paleta_sau['Contagem'], textposition='outside', showlegend=False)
        
        
        # Exibir o gráfico no Streamlit
        graf1.plotly_chart(figbar2, use_container_width=False)

        graf2.write('saufeitas que falaram "Sim" para a classificação Étnico Racial')
        # Criar o gráfico de barras lado a lado
        figbar3 = px.bar(contagem_autodeclara_sim_sau, x='Raça/paleta', y='Contagem',
                    labels={'Raça/paleta': 'Raça/Cor', 'value': 'Contagem'},
                    width=450,
                    height=450,
                    color_discrete_sequence=azul
            )
        figbar3.update_traces(text=contagem_autodeclara_sim_sau['Contagem'], textposition='outside', showlegend=False)

        
        # Exibir o gráfico no Streamlit
        graf2.plotly_chart(figbar3, use_container_width=False)

# ----------------------------------------------------------------------