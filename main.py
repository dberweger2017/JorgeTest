import streamlit as st

st.title("Calculadora")
choice = st.selectbox("Que quieres hacer?", ["Suma", "Resta", "Multiplicacion", "Division", "Media"])
num1 = st.number_input("Escge un primer numero:", step = 1)
num2 = st.number_input("Escoge u segundo numero:", step = 1)

resultado = None
if st.button("Calcular"):
    if choice == "Suma":
        resultado = num1 + num2
    elif choice == "Resta":
        resultado = num1 - num2
    elif choice == "Multiplicacion":
        resultado = num1 * num2
    elif choice == "Division":
        resultado = num1/num2

    st.write("El resultado es " + str(resultado))
#def calculadora
