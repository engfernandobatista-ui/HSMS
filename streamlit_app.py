import streamlit as st
import datetime

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.title("Inspeção do HMS")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

d = st.date_input("Embarcação", )
d = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6))

                  
