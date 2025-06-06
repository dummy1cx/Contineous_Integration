import streamlit as st
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power")

##  get user input

n = st.number_input("Enter an integer", value = 1, step = 1)


# calculate_results

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#Display results

st.write(f"The square of the number {n} is : {square}")
st.write(f"The cube of the number {n} is : {cube}")
st.write(f"The fifth power of the number {n} is : {fifth_power}")
         