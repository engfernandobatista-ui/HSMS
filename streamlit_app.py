import streamlit as st
import datetime

st.title("Inspeção do HMS")

title = st.text_input(" Embarcação", "")
st.write("The current movie title is", title)

d = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6))

                  
