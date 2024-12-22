import streamlit as st

st.title("Halaman Dashboard")

def total():
    total_nabung = sum(t['jumlah'] for t in st.session_state['total_semua'] if t ['Tipe'] == 'Menabung')

    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("Total Menabung Anda", f"Rp.{total_nabung}")