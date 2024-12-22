import streamlit as st

#st.title("Hello Masbro")
#st.write("Apa Kabar") 
#st.image("images.jpg", caption="Ini gambar")

# Sidebar Direktory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
  {
    "Menu Utama":[dashboard],
    "Transaksi": [nabung]
  }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()