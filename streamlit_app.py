import streamlit as st
import datetime

st.title("Inspeção do HMS")

title = st.text_input(" Embarcação", "")
title = st.text_input("Nota", "")
d = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6), format="DD/MM/YYYY")

st.header("1. Inspeção", divider="gray",text_alignment="center")
genre = st.radio(
    "A identificação do painel e dos seus componentes estão visíveis e em bom estado de conservação (interno e externo)?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "O equipamento apresentou algum alarme?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "A configuração dos equipamentos está conforme especificação do fabricante?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Foram detectados sinais de umidade, poeira ou sujeira no gabinete?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Existe sinal de corrosão e/ou ferrugem nos componentes do sistema?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Há prensa-cabos frouxos, quebrados, não instalados, etc.?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "O gabinete do HSMS está selado e limpo?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Suporte e fixação em bom estado de conservação e adequados aos componentes?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Foi verificado se as fixações do gabinete estão no lugar e seguras?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
genre = st.radio(
    "Foi verificado se as roscas estão lubrificadas no sensor SBSG?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
st.header("2. Considerações finais", divider="gray",text_alignment="center")
genre = st.radio(
    "Todas as anormalidades encontradas na inspeção foram sanadas?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
st.header("3. Comentários", divider="gray",text_alignment="center")

                  
