# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:11:06 2023

@author: Petra Izeboud
"""

# %%

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


def create_bar_chart(df):
    st.bar_chart(df)

df = pd.DataFrame(
            np.random.randn(10,4),
            columns=['2011', '2012', '2013', '2014'])

st.markdown(
    """
    # Show your dataframe
    """)
    
st.area_chart(df)

checkbox = st.checkbox("Show area chart", value=True)
if checkbox:
    st.write('clicked checkbox')
    

st.button('Create bar chart', on_click=create_bar_chart, args=(df, ))



# %%

