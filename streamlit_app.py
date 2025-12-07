import streamlit as st
import datetime

st.title("Inspeção do HMS")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.write ("Embarcação")
d = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6))

                  
