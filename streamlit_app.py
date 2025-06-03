# app.py

import streamlit as st

# Simulasi senarai model Mercedes-Benz Malaysia
mercedes_models = [
    "A-Class Hatchback",
    "A-Class Sedan",
    "C-Class Sedan",
    "E-Class Sedan",
    "S-Class Sedan",
    "GLA SUV",
    "GLB SUV",
    "GLC SUV",
    "GLE SUV",
    "GLS SUV",
    "AMG GT",
    "EQE Sedan",
    "EQS Sedan",
    "EQB SUV",
    "EQC SUV",
]

# Streamlit App
st.set_page_config(page_title="Mercedes-Benz Car Finder", page_icon="🚗")
st.title("🚗 Mercedes-Benz Car Model Search (Malaysia)")
st.markdown("[Laman rasmi Mercedes-Benz Malaysia](https://www.mercedes-benz.com.my/)")

# Search box
query = st.text_input("🔍 Cari model (contoh: GLC, EQ, Sedan):")

# Search logic
if query:
    results = [model for model in mercedes_models if query.lower() in model.lower()]
    if results:
        st.success(f"{len(results)} model dijumpai:")
        for model in results:
            st.markdown(f"✅ {model}")
    else:
        st.warning("❌ Tiada model ditemui.")
else:
    st.info("Sila masukkan kata kunci carian.")

# Optional styling / footer
st.markdown("---")
st.caption("Dibina dengan ❤️ oleh Streamlit. Maklumat model berdasarkan laman rasmi Mercedes-Benz Malaysia.")
