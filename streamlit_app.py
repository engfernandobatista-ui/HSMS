import streamlit as st
import datetime

dados_dict = {}
st.title("Inspeção do HMS")

dados_dict["Embarcação"] = st.text_input(" Embarcação", "")
dados_dict["Nota"] = st.text_input("Nota", "")
dados_dict["Horas"] = st.number_input("Duração da atividade (horas):", format="%0.1f")
dados_dict["Data"] = st.date_input("Data de término da tarefa", datetime.date(2019, 7, 6), format="DD/MM/YYYY")

st.header("1. Inspeção", divider="gray",text_alignment="center")
dados_dict["Pergunta_1"] = st.radio(
    "A identificação do painel e dos seus componentes estão visíveis e em bom estado de conservação (interno e externo)?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_2"] = st.radio(
    "O equipamento apresentou algum alarme?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_3"] = st.radio(
    "A configuração dos equipamentos está conforme especificação do fabricante?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_4"] = st.radio(
    "Foram detectados sinais de umidade, poeira ou sujeira no gabinete?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_5"] = st.radio(
    "Existe sinal de corrosão e/ou ferrugem nos componentes do sistema?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_6"] = st.radio(
    "Há prensa-cabos frouxos, quebrados, não instalados, etc.?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_7"] = st.radio(
    "O gabinete do HSMS está selado e limpo?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_8"] = st.radio(
    "Suporte e fixação em bom estado de conservação e adequados aos componentes?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_9"] = st.radio(
    "Foi verificado se as fixações do gabinete estão no lugar e seguras?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
dados_dict["Pergunta_10"] = st.radio(
    "Foi verificado se as roscas estão lubrificadas no sensor SBSG?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
st.header("2. Considerações finais", divider="gray",text_alignment="center")
dados_dict["Pergunta_11"] = st.radio(
    "Todas as anormalidades encontradas na inspeção foram sanadas?",
    ["OK", "NOK", "N/A"],
    index=None,horizontal=True
)
st.header("3. Comentários", divider="gray",text_alignment="center")
dados_dict["Pergunta_12"] = st.text_input("")
st.header("4. Condição", divider="gray",text_alignment="center")
dados_dict["Pergunta_13"] = st.radio(
    "Condição Resultante do Instrumento/Equipamento?",
    ["GOOD", "ADJU", "MALF", "MFAR"],
    index=None,horizontal=True
)
st.header("5. Classificação", divider="gray",text_alignment="center")
dados_dict["Pergunta_14"] = st.radio(
    "Classificação da falha de impacto?",
    ["Falha incipiente", "Falha degradada", "Falha crítica"],
    index=None,horizontal=True
)
st.header("6. Função", divider="gray",text_alignment="center")
dados_dict["Pergunta_15"] = st.multiselect(
    "Função do executante?",
    ["System Tech", "Instrumentista", "Lead I&C"],
    max_selections=1,
    accept_new_options=True,
)
dados_dict["Pergunta_16"] = st.text_input(" Nome do executante", "")
options = st.multiselect(
    "Função do aprovador?",
    ["System Tech", "Instrumentista", "Lead I&C"],
    max_selections=1,
    accept_new_options=True,
)
dados_dict["Pergunta_17"] = st.text_input(" Nome do aprovador", "")

st.header("7. Anexos", divider="gray",text_alignment="center")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
if st.button("Enviar:"):
    st.dataframe(dados_dict)


# Comando para selecionar planilha
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def carregar_planilha():
    # Abre um diálogo para escolher o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    
    if arquivo:
        try:
            # Carrega a planilha usando pandas
            df = pd.read_excel(arquivo)
            # Exibe as primeiras linhas do DataFrame
            print(df.head())
            messagebox.showinfo("Sucesso", "Planilha carregada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a planilha: {e}")

# Cria a janela principal
root = tk.Tk()
root.title("Carregar Planilha Excel")

# Cria um botão para carregar a planilha
botao_carregar = tk.Button(root, text="Escolher Planilha", command=carregar_planilha)
botao_carregar.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()
