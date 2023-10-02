import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import locale
locale.setlocale(locale.LC_ALL, "C")

# Configurando a página
st.set_page_config(
    page_title="Dashboard Adidas",
    page_icon="\\workspaces\\datascience\\dashboard_adidas\\logoadidas.png",
    layout="wide",
)

# Define a cor de fundo da página
st.markdown(
    """
    <style>
    body {
        background-color: #002D72; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Lendo o arquivo CSS
css_code = st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');

* {
    margin: 0; /* Remove todas as margens iniciais */
    font-family: 'Inter', sans-serif; /* Font do component, remova para usar a font nativa do PBI */
}


table { 
    width: 700px; /* Largura da tabela, modifque conforme número de colunas */ 
    border-collapse: collapse;
}
th { /* th - é o header da tabela */
    background-color: #313A40; /* Cor do cabeçalho */
    color: #F2F2F2; /* Cor do texto do cabeçalho */
    
    padding: 1rem;
    border-bottom: 2px solid #2fb3d8;

    text-align: left;
    font-size: 0.875rem;
    
    line-height: 1.2;
    width: auto;
}
th:first-child {
    border-top-left-radius: 8px; /* Aplica borda superior esquerdo na primeira coluna */
    padding-left: 1.5rem;
}
th:last-child {
    border-top-right-radius: 8px; /* Aplica borda superior direito na ultima coluna */
    padding-right: 1.5rem;
}
td {
    cursor: pointer;
    background-color: #0E1117; /* Cor das linhas */
    border-top: 1px solid rgb(221, 221, 221);  /* Cor das linhas separadoras*/
    padding: 1rem; /* preenchimento ao redor */
    font-size: 0.900rem; /* font dos textos das linhas */
    line-height: 1.2; /* Altura dos textos das linhas */
    width: auto; /* largura automática das linhas */
}
td:first-child {
    padding-left: 1.5rem;
}

td:last-child {
    padding-right: 1.5rem;
}

/* Todas linhas - ao passar o mouse */

td:hover {
    background: #313A40; /* Cor ao passar o mouse */
    z-index: 1;
    transition: 300ms; /* Tempo para esmaecer */
}

    </style>
    """,
    unsafe_allow_html=True
)

# Renderizando o CSS usando st.markdown()
st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)

# Cores personalizadas
cor1 = ["#A9D943"]

# Lendo o conjunto de dads
dataframe = pd.read_excel("\\workspaces\\datascience\\dashboard_adidas\\sales_adidas.xlsx")


# ------------------------------------------------

# Criando a config da página
col1, col2 = st.columns(2)
#col1.image("/workspaces/datascience/dashboard_adidas/logoadidas.png", use_column_width=False, width=85)
col1.markdown(
    "<h1 style='font-family: Montserrat, sans-serif; font-weight: normal;'>Dashboard das <span style='font-weight: bold;'>Vendas Adidas</span></h2>",
    unsafe_allow_html=True,
)
col1.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    body {
        background-color: #002D72; /* Substitua pela cor desejada em formato hexadecimal */
    }
    </style>
    """,
    unsafe_allow_html=True)


# Criando os 3 primeiros cards
# Total de vendas
total_vendas = round(dataframe["Total Sales"].sum(), 2)
total_vendas_formatado = f"${total_vendas:,.2f}"
# Produto mais vendido
produto_mais_vendido = dataframe["Product"].value_counts().idxmax()
# Varejista que mais vendeu
varejista_top = dataframe["Retailer"].value_counts().idxmax()

col4, col5, col6 = st.columns(3)
col4.metric("Total de vendas", total_vendas)
col5.metric("Produto mais vendido", produto_mais_vendido)
col6.metric("Varejista que mais vendeu", varejista_top)

st.markdown("""---""")

# ------------------------------------------------


# PRIMEIRA FIGURA
col7, col8 = st.columns(2)

dataframe["Month"] = dataframe["Invoice Date"].dt.strftime("%Y-%m")
vendas_mes = dataframe.groupby("Month")["Total Sales"].sum().reset_index()
graf_vendas_mes = px.area(
    vendas_mes,
    x="Month",
    y="Total Sales",
    title="Total de vendas por mês",
    color_discrete_sequence=cor1,
)

# Exibindo o primeiro gráfico na coluna 7
col7.plotly_chart(graf_vendas_mes)

# ------------------------------------------------

# SEGUNDA FIGURA
vendas_regiao = dataframe.groupby("Region")["Total Sales"].sum().reset_index()
graf_vendas_regiao = px.bar(
    vendas_regiao,
    x="Region",
    y="Total Sales",
    title="Total de vendas por região",
    color_discrete_sequence=cor1,
)

# Exibindo o segundo gráfico na coluna 8
col8.plotly_chart(graf_vendas_regiao)

# ------------------------------------------------
col9, col10 = st.columns(2)
# TERCEIRA FIGURA

# Agrupando total de vendas por estado
vendas_por_estado = (
    dataframe.groupby("State")["Total Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Total Sales", ascending=False)
)

with col9:
    st.write("**Total de Vendas por Estados**")
    # Defina um tamanho máximo para a tabela e adicione uma barra de rolagem
    table_html = f"<div style='max-height: 300px; overflow-y: auto;'><table><thead><tr><th>Estados</th><th>Total de Vendas</th></tr></thead><tbody>"
    for _, row in vendas_por_estado.iterrows():
        total_sales_formatado = row["Total Sales"]
        total_sales_formatado_com_cifrao = (
            f"${total_sales_formatado:,.2f}"  # Adicione o cifrão
        )
        table_html += f"<tr><td>{row['State']}</td><td>{total_sales_formatado_com_cifrao}</td></tr>"

    table_html += "</tbody></table></div>"

    # Exiba a tabela personalizada
    st.markdown(table_html, unsafe_allow_html=True)
    col9.markdown("<br>", unsafe_allow_html=True)


# ------------------------------------------------
# QUARTA FIGURA

# Crie um componente de layout no Streamlit
# Agrupando e criando ranking de total de vendas por produto
vendas_por_produto = (
    dataframe.groupby("Product")["Total Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Total Sales", ascending=False)
)
vendas_por_produto["Ranking"] = (
    vendas_por_produto["Total Sales"].rank(ascending=False, method="min").astype(int)
)
vendas_por_produto["Total Sales"] = vendas_por_produto["Total Sales"].apply(
    lambda x: f"${x:,.2f}"
)
vendas_por_produto = vendas_por_produto[
    ["Ranking", "Product", "Total Sales"]
].reset_index(drop=True)
with col10:
    # Crie um DataFrame a partir de vendas_por_estado
    df_produto = pd.DataFrame(vendas_por_produto)

    # Remova todos os caracteres não numéricos da coluna "Total Sales" e converta para float
    df_produto["Total Sales"] = df_produto["Total Sales"].str.replace('[^\d.]', '', regex=True).astype(float)

    # Calcule a frequência relativa
    df_produto['Relative Frequency'] = df_produto['Total Sales'] / df_produto['Total Sales'].sum()

    # Arredonde o valor da frequência relativa para duas casas decimais
    df_produto['Relative Frequency'] = df_produto['Relative Frequency'].round(2)

    # Ordene o DataFrame pelo valor da frequência relativa em ordem decrescente
    df_produto = df_produto.sort_values(by='Relative Frequency', ascending=False)

    # Configure o gráfico de barras horizontais com Plotly Express
    visual1 = px.bar(
        df_produto,
        x="Relative Frequency",  # Use a frequência relativa no eixo x
        y="Product",
        orientation="h",
        text=df_produto["Relative Frequency"].apply(lambda x: f"{x}%"),  # Adicione o símbolo "%" nas porcentagens
    )

    # Personalize o layout do gráfico
    visual1.update_layout(
        title="Frequência Relativa de Vendas por Produto",
        xaxis_tickformat="%",  # Exibir valores no eixo x como porcentagens
        xaxis_title="",  # Remova o título do eixo x
        showlegend=False,  # Oculte a legenda
        height=400,
    )

    # Defina a cor das barras para verde
    visual1.update_traces(
        marker=dict(color="#A9D943"),
        insidetextfont=dict(size=14, color="#0E1117"),  # Cor do texto dentro das barras
    )

    visual1.update_yaxes(tickfont=dict(size=16))
    visual1.update_xaxes(showline=False, showticklabels=False)  # Remova os rótulos do eixo x
    st.plotly_chart(visual1)

# QUINTA FIGURA

# Crie um componente de layout no Streamlit
# Agrupando e criando ranking de total de vendas por sales method
# vendas_por_metodo = dataframe.groupby('Sales Method')['Total Sales'].sum().reset_index().sort_values(by='Total Sales', ascending=False)
# vendas_por_metodo['Ranking'] = vendas_por_metodo['Total Sales'].rank(ascending=False, method='min').astype(int)
# vendas_por_metodo['Total Sales'] = vendas_por_metodo['Total Sales'].apply(lambda x: f'${x:,.2f}')
# vendas_por_metodo = vendas_por_metodo[['Ranking', 'Sales Method', 'Total Sales']].reset_index(drop=True)
# with col10:
#     # Crie um DataFrame a partir de vendas_por_estado
#     df_metodo = pd.DataFrame(vendas_por_metodo)

#     # Configure o gráfico de barras horizontais com Plotly Express
#     visual2 = px.bar(df_metodo, x='Total Sales', y='Sales Method', orientation='h', text='Total Sales')

#     # Personalize o layout do gráfico
#     visual2.update_layout(
#         title='Total de Vendas por Estado',
#         xaxis_title='Total de Vendas',
#         yaxis_title='Estado',
#         yaxis_categoryorder='total ascending',  # Ordene os estados pelo total de vendas
#         xaxis_tickprefix='R$',  # Adicione o prefixo R$ ao eixo X
#         showlegend=False,  # Oculte a legenda
#         height=300,
#     )

#     # Exiba o gráfico no Streamlit
#     st.plotly_chart(visual2)
