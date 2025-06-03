# app.py

import streamlit as st

st.set_page_config(page_title="Basic Calculator", page_icon="🧮")

st.title("🧮 Basic Calculator")
st.markdown("Perform basic arithmetic operations.")

# User inputs
num1 = st.number_input("Enter first number:", format="%.2f")
operation = st.selectbox("Select operation:", ["+", "-", "*", "/"])
num2 = st.number_input("Enter second number:", format="%.2f")

# Calculate based on operation
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b if b != 0 else "Cannot divide by zero"
    except Exception as e:
        return f"Error: {e}"

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
