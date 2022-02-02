import streamlit as st

resultado = None
num1 = None
num2 = None
numMedia = []

st.title("Calculadora")
choice = st.selectbox("Que quieres hacer?", ["Suma", "Resta", "Multiplicacion", "Division", "Media"])

#Inputs
if choice == "Suma" or choice == "Resta" or choice == "Multiplicacion" or choice == "Division":
    num1 = st.number_input("Escge un primer numero:", step=1)
    num2 = st.number_input("Escoge u segundo numero:", step=1)
elif choice == "Media":
    numMediaImput = st.slider("De cuantos numeros quieres hacer la media?", min_value=2, max_value=20, value = 5)
    for i in range(numMediaImput):
        numMedia += [st.number_input("Escge un primer numero:", step=1, key = i)]

#Calculo
if st.button("Calcular"):
    if choice == "Suma":
        resultado = num1 + num2
    elif choice == "Resta":
        resultado = num1 - num2
    elif choice == "Multiplicacion":
        resultado = num1 * num2
    elif choice == "Division":
        resultado = num1/num2
    elif choice == "Media":
        resultado = 0
        for i in range(len(numMedia)):
            resultado += numMedia[i]
        resultado = resultado / len(numMedia)

    st.write("El resultado es " + str(resultado))
