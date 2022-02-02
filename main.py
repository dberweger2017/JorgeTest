import streamlit as st

st.title("Calculadora")
choice = st.selectbox("Que quieres hacer?", ["Suma", "Resta", "Multiplicacion", "Division", "Media"])
num1 = st.number_input("Escge un primer numero:", int)
num2 = st.number_input("Escoge u segundo numero:")

resultado = None
if st.button("Calcular"):
     if choice == "Suma":
         resultado = num1 + num2
     elif choice == "resta":
         resultado = num1 - num2
    
     
     st.write("El resultado es " + str(resultado))
#def calculadora()
