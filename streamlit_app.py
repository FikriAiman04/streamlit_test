import streamlit as st
import base64

# ---- Set custom dragon background using base64 image ----
def set_background(base64_str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Paste your base64 string here (replace the content below with your actual image data)
dragon_base64 = "YOUR_BASE64_STRING_HERE"
set_background(dragon_base64)

# ---- App Title and Welcome ----
st.title("🧮 Enhanced Calculator with Dragon Theme")
st.write("Welcome to the **Dragon-Themed Streamlit Calculator App!**")

# ---- Basic Calculator ----
st.header("Basic Calculator")

num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"

st.write(f"**Result:** {result}")

# ---- Number System Converter ----
st.header("Number System Converter")

int_input = st.number_input("Enter an integer to convert:", value=0, step=1)

binary = bin(int(int_input))[2:]
decimal = int(int_input)
hexadecimal = hex(int(int_input))[2:].upper()

st.subheader("Conversions")
st.write(f"**Binary:** {binary}")
st.write(f"**Decimal:** {decimal}")
st.write(f"**Hexadecimal:** {hexadecimal}")







