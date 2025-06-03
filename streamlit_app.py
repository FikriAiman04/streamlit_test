# app.py

import streamlit as st

# Simulasi data model dan gambar
mercedes_data = {
    "A-Class Hatchback": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/a-class/hatchback/v177-refresh/overview/mercedes-benz-a-class-hatchback-v177-overview-696x392-02-2023.png",
    "A-Class Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/a-class/sedan/v177-refresh/overview/mercedes-benz-a-class-sedan-v177-overview-696x392-02-2023.png",
    "C-Class Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/c-class/sedan/v206/overview/mercedes-benz-c-class-v206-overview-696x392-07-2021.png",
    "E-Class Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/e-class/sedan/w213-facelift/overview/mercedes-benz-e-class-sedan-w213-overview-696x392-09-2020.png",
    "S-Class Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/s-class/sedan/v223/overview/mercedes-benz-s-class-v223-overview-696x392-12-2020.png",
    "GLA SUV": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/gla/suv/h247/overview/mercedes-benz-gla-h247-overview-696x392-04-2020.png",
    "GLC SUV": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/glc/suv/x254/overview/mercedes-benz-glc-x254-overview-696x392-06-2022.png",
    "GLE SUV": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/gle/suv/v167/overview/mercedes-benz-gle-v167-overview-696x392-10-2020.png",
    "GLS SUV": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/gls/suv/x167/overview/mercedes-benz-gls-x167-overview-696x392-11-2020.png",
    "EQE Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/eqe/sedan/v295/overview/mercedes-benz-eqe-v295-overview-696x392-12-2021.png",
    "EQS Sedan": "https://www.mercedes-benz.com.my/content/dam/hq/passengercars/models/eqs/sedan/v297/overview/mercedes-benz-eqs-v297-overview-696x392-12-2021.png",
}

# Streamlit App
st.set_page_config(page_title="Mercedes-Benz Car Search", page_icon="🚗")
st.title("🚗 Mercedes-Benz Car Model Search (Malaysia)")
st.markdown("[Laman rasmi Mercedes-Benz Malaysia](https://www.mercedes-benz.com.my/)")

# Search box
query = st.text_input("🔍 Cari model (contoh: GLC, Sedan, EQ):")

# Logic carian dan paparan
if query:
    # Cari model yang padan dengan kata kunci
    matches = {model: img for model, img in mercedes_data.items() if query.lower() in model.lower()}

    if matches:
        st.success(f"{len(matches)} model dijumpai:")
        for model, img_url in matches.items():
            st.subheader(model)
            st.image(img_url, width=400)
    else:
        st.warning("❌ Tiada model ditemui.")
else:
    st.info("Sila masukkan kata kunci carian.")
