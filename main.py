import streamlit as st

st.title("Calculadora")
chice = st.selectbox("Que quieres hacer?", ["Suma", "Resta", "Multiplicacion", "Division", "Media"])
num1 = st.number_input("Escge un primer numero:")
num2 = st.number_input("Escoge u segundo numero:")
#def calculadora()
