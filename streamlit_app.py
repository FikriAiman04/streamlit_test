import streamlit as st

# Set the app title
st.title("🧮 Enhanced Calculator with Number System Converter")

# Welcome message
st.write("Welcome to the Streamlit Calculator App!")

# --- Basic Calculator Section ---
st.header("Basic Calculator")

# Input numbers
num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

# Select operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"

# Display result
st.write(f"**Result:** {result}")

# --- Number System Converter Section ---
st.header("Number System Converter")

# Input a number (as integer)
int_input = st.number_input("Enter an integer to convert:", value=0, step=1)

# Convert to binary, decimal, and hexadecimal
binary = bin(int(int_input))[2:]
decimal = int(int_input)
hexadecimal = hex(int(int_input))[2:].upper()

# Display conversions
st.subheader("Conversions")
st.write(f"**Binary:** {binary}")
st.write(f"**Decimal:** {decimal}")
st.write(f"**Hexadecimal:** {hexadecimal}")






