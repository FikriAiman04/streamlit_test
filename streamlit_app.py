import streamlit as st

# Set the app title
st.title("🧮 Simple Calculator")

# Add a welcome message
st.write("Welcome to the Streamlit Calculator App!")

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





