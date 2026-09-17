# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:11:06 2023

@author: Petra Izeboud
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Interactieve grafieken")

aantal = st.slider("Hoeveel maanden wil je zien?", 1, 12, 6)

df = pd.DataFrame(
    np.random.randn(12, 2),
    columns=["Temperatuur", "Neerslag"]
)

df = df.iloc[:aantal]


col1, col2 = st.columns(2)

with col1:
    st.subheader("Temperatuur")
    st.line_chart(df["Temperatuur"])

with col2:
    st.subheader("Neerslag")
    st.bar_chart(df["Neerslag"])
