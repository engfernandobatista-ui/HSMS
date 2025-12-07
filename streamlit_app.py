import streamlit as st
import datetime

st.title("Inspeção do HMS")

title = st.text_input(" Embarcação", "")
title = st.text_input("Nota", "")

st.header("Inspeção", divider="gray"), text_alignment="left"
genre = st.radio(
    "A identificação do painel e dos seus componentes estão visíveis e em bom estado de conservação (interno e externo)?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)


d = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6))

                  
